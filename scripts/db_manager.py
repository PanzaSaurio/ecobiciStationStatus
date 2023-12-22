#db_manager.py

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
                        raise TypeError(f"Error: se esperaba un diccionario, se recibió: {type(station)}")

                    required_keys = ['station_id', 'num_bikes_available', 'num_mechanical_bikes_available',
                                     'num_ebikes_available', 'num_bikes_disabled', 'num_docks_available',
                                     'num_docks_disabled', 'last_reported', 'is_charging_station', 'status',
                                     'is_installed', 'is_renting', 'is_returning', 'traffic']
                    
                    if not all(key in station for key in required_keys):
                        raise ValueError(f"Error: faltan claves en los datos de la estación: {station}")

                    insert_query = """
                    INSERT INTO {}.ecobici_stations (
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
                        FROM {}.ecobici_stations
                        WHERE station_id = %s AND last_reported = %s
                    );
                    """.format(config['REDSHIFT_SCHEMA'], config['REDSHIFT_SCHEMA'])

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

                conn.commit()
    except Exception as e:
        raise Exception(f"Error al procesar o insertar datos en la base de datos: {e}")


def insert_vehicle_data_to_db(config, processed_vehicle_data):
    conn_str = (f"dbname='{config['REDSHIFT_DB']}' user='{config['REDSHIFT_USER']}' "
                f"host='{config['REDSHIFT_ENDPOINT']}' password='{config['REDSHIFT_PASS']}' "
                f"port='{config['REDSHIFT_PORT']}'")

    try:
        with psycopg2.connect(conn_str) as conn:
            with conn.cursor() as cur:
                for vehicle in processed_vehicle_data:
                    if not isinstance(vehicle, dict):
                        raise TypeError(f"Error: se esperaba un diccionario, se recibió: {type(vehicle)}")

                    required_keys = ['route_id', 'latitude',
                        'longitude','speed','timestamp','id',
                        'direction','agency_name','agency_id',
                        'route_short_name','tip_id','trip_headsign']
                    
                    if not all(key in vehicle for key in required_keys):
                        raise ValueError(f"Error: faltan claves en los datos de los vehiculos: {vehicle}")

                    insert_query = """
                    INSERT INTO {}.vehicle_positions (
                        route_id,
                        latitude,
                        longitude,
                        speed,
                        timestamp,
                        id,
                        direction,
                        agency_name,
                        agency_id,
                        route_short_name,
                        tip_id,
                        trip_headsign
                    )
                    SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    WHERE NOT EXISTS (
                        SELECT 1
                        FROM {}.vehicle_positions
                        WHERE id = %s AND timestamp = %s
                    );
                    """.format(config['REDSHIFT_SCHEMA'], config['REDSHIFT_SCHEMA'])

                    print("SQL Query:", insert_query)

                    print("Data:", (vehicle.get('route_id'),
                        vehicle.get('latitude'),
                        vehicle.get('longitude'),
                        vehicle.get('speed'),
                        vehicle.get('timestamp'),
                        vehicle.get('id'),
                        vehicle.get('direction'),
                        vehicle.get('agency_name'),
                        vehicle.get('agency_id'),
                        vehicle.get('route_short_name'),
                        vehicle.get('tip_id'),
                        vehicle.get('trip_headsign')
                    ))

                    cur.execute(insert_query, (
                        vehicle.get('route_id'),
                        vehicle.get('latitude'),
                        vehicle.get('longitude'),
                        vehicle.get('speed'),
                        vehicle.get('timestamp'),
                        vehicle.get('id'),
                        vehicle.get('direction'),
                        vehicle.get('agency_name'),
                        vehicle.get('agency_id'),
                        vehicle.get('route_short_name'),
                        vehicle.get('tip_id'),
                        vehicle.get('trip_headsign'),
                        vehicle.get('id'),        
                        vehicle.get('timestamp')
                    ))

                conn.commit()
    except Exception as e:
        raise Exception(f"Error al procesar o insertar datos en la base de datos: {e}")