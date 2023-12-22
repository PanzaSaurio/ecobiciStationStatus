#data_processor.py

import pandas as pd
from datetime import datetime
from scripts.email_alert import send_email

def unix_to_readable(unix_timestamp):
    """Convertir timestamp unix a datetime."""
    return pd.to_datetime(unix_timestamp, unit='s') if unix_timestamp else None

def process_data(data,email):
    processed_data = []
    for station in data['data']['stations']:
        processed_station = {
            'station_id': station.get('station_id'),
            'num_bikes_available': station.get('num_bikes_available'),
            'num_bikes_disabled': station.get('num_bikes_disabled'),
            'num_docks_available': station.get('num_docks_available'),
            'num_docks_disabled': station.get('num_docks_disabled'),
            'last_reported': unix_to_readable(station.get('last_reported')),
            'is_charging_station': station.get('is_charging_station'),
            'status': station.get('status'),
            'is_installed': station.get('is_installed'),
            'is_renting': station.get('is_renting'),
            'is_returning': station.get('is_returning'),
            'traffic': station.get('traffic'),
            'num_mechanical_bikes_available': station.get('num_bikes_available_types', {}).get('mechanical'),
            'num_ebikes_available': station.get('num_bikes_available_types', {}).get('ebike')
        }
        processed_data.append(processed_station)

        if processed_station.get('status') == "END_OF_LIFE":
            # def send_email(station, status, email):
            send_email(processed_station.get('station_id') 
                       ,processed_station.get('status') 
                       ,email)
            

    return processed_data

def process_vehicle_data_task(vehicle_data):
    processed_vehicles = []
    for vehicle in vehicle_data:
        timestamp = unix_to_readable(vehicle.get('timestamp'))
        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S') if timestamp else None        
        processed_vehicle = {
            'route_id': vehicle.get('route_id'),
            'latitude': vehicle.get('latitude'),
            'longitude': vehicle.get('longitude'),
            'speed': vehicle.get('speed'),
            'timestamp': formatted_timestamp,
            'id': vehicle.get('id'),
            'direction': vehicle.get('direction'),
            'agency_name': vehicle.get('agency_name'),
            'agency_id': vehicle.get('agency_id'),
            'route_short_name': vehicle.get('route_short_name'),
            'tip_id': vehicle.get('tip_id'),
            'trip_headsign': vehicle.get('trip_headsign')
        }
        processed_vehicles.append(processed_vehicle)

    return processed_vehicles