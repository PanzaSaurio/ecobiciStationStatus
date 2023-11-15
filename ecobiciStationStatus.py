import json
import pandas as pd
import requests
import psycopg2
from datetime import datetime

def unix_to_readable(unix_timestamp):
    """Convertir timestamp unix a datetime."""
    return pd.to_datetime(unix_timestamp, unit='s')

# Cargo las credenciales y configuraciones desde el archivo
with open('credentials.json', 'r') as file:
    config = json.load(file)

# Creo la URL completa
url = f"{config['BASE_URL']}{config['ENDPOINT']}?client_id={config['CLIENT_ID']}&client_secret={config['CLIENT_SECRET']}"

response = requests.get(url)
data = response.json()

# Proceso los datos del JSON
processed_data = []
for station in data['data']['stations']:
    if 'last_reported' in station:
        station['last_reported'] = unix_to_readable(station['last_reported']) if pd.notnull(station['last_reported']) else None
    if 'num_bikes_available_types' in station:
        station['num_mechanical_bikes_available'] = station['num_bikes_available_types']['mechanical']
        station['num_ebikes_available'] = station['num_bikes_available_types']['ebike']
    else:
        station['num_mechanical_bikes_available'] = None
        station['num_ebikes_available'] = None
    processed_data.append(station)

df = pd.DataFrame(processed_data)
df = df.drop_duplicates(subset='station_id', keep='last')

# Reemplazo los NaT con la fecha y hora actuales
fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
df['last_reported'] = df['last_reported'].fillna(fecha_hora_actual)

# Creo la cadena de conexión a Redshift
conn_str = (f"dbname='{config['REDSHIFT_DB']}' user='{config['REDSHIFT_USER']}' "
            f"host='{config['REDSHIFT_ENDPOINT']}' password='{config['REDSHIFT_PASS']}' "
            f"port='{config['REDSHIFT_PORT']}'")

print(f"Cantidad de registros recuperados: {len(df)}")

# Realizo el insert en Redshift
try:
    with psycopg2.connect(conn_str) as conn:
        with conn.cursor() as cur:
            for index, row in df.iterrows():
                insert_query = f"""
                INSERT INTO {config['REDSHIFT_SCHEMA']}.ecobici_stations (
                    station_id,
                    num_bikes_available,
                    num_mechanical_bikes_available,
                    num_ebikes_available,
                    num_bikes_disabled,
                    num_docks_available,
                    num_docks_disabled,
                    last_reported,
                    is_charging_station,
                    status,
                    is_installed,
                    is_renting,
                    is_returning,
                    traffic
                )
                SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM {config['REDSHIFT_SCHEMA']}.ecobici_stations
                    WHERE station_id = %s AND last_reported = %s
                );
                """
                try:
                    cur.execute(insert_query, (
                        row['station_id'],
                        row['num_bikes_available'],
                        row['num_mechanical_bikes_available'],
                        row['num_ebikes_available'],
                        row['num_bikes_disabled'],
                        row['num_docks_available'],
                        row['num_docks_disabled'],
                        row['last_reported'],
                        row['is_charging_station'],
                        row['status'],
                        row['is_installed'],
                        row['is_renting'],
                        row['is_returning'],
                        row['traffic'],
                        row['station_id'],  
                        row['last_reported'] 
                    ))
                except Exception as e:
                    print(f"Error al insertar station_id {row['station_id']}: {e}")

            conn.commit()
except Exception as e:
    print(f"Error de conexión general: {e}")
