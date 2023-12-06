import psycopg2

def insert_data_to_db(config, processed_data):
    conn_str = (f"dbname='{config['REDSHIFT_DB']}' user='{config['REDSHIFT_USER']}' "
                f"host='{config['REDSHIFT_ENDPOINT']}' password='{config['REDSHIFT_PASS']}' "
                f"port='{config['REDSHIFT_PORT']}'")

    try:
        with psycopg2.connect(conn_str) as conn:
            with conn.cursor() as cur:
                for station in processed_data:
                    if not isinstance(station, dict):
                        print(f"Error: se esperaba un diccionario, se recibió: {type(station)}")
                        continue

                    required_keys = ['station_id', 'num_bikes_available', 'num_mechanical_bikes_available',
                                     'num_ebikes_available', 'num_bikes_disabled', 'num_docks_available',
                                     'num_docks_disabled', 'last_reported', 'is_charging_station', 'status',
                                     'is_installed', 'is_renting', 'is_returning', 'traffic']
                    
                    if not all(key in station for key in required_keys):
                        print(f"Error: faltan claves en los datos de la estación: {station}")
                        continue

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
                            station.get('station_id'),
                            station.get('num_bikes_available'),
                            station.get('num_mechanical_bikes_available'),
                            station.get('num_ebikes_available'),
                            station.get('num_bikes_disabled'),
                            station.get('num_docks_available'),
                            station.get('num_docks_disabled'),
                            station.get('last_reported'),
                            station.get('is_charging_station'),
                            station.get('status'),
                            station.get('is_installed'),
                            station.get('is_renting'),
                            station.get('is_returning'),
                            station.get('traffic'),
                            station.get('station_id'),  
                            station.get('last_reported')
                        ))
                    except Exception as e:
                        print(f"Error al insertar station_id {station.get('station_id')}: {e}")

                conn.commit()
    except Exception as e:
        print(f"Error de conexión general: {e}")
