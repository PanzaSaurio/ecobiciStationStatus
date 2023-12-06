import pandas as pd
from datetime import datetime

def unix_to_readable(unix_timestamp):
    """Convertir timestamp unix a datetime."""
    return pd.to_datetime(unix_timestamp, unit='s') if unix_timestamp else None

def process_data(data):
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

    return processed_data
