# ecobiciStationStatus.py

from scripts.api_client import get_api_data
from scripts.config_loader import load_config
from scripts.data_processor import process_data
from scripts.db_manager import insert_data_to_db

def process_station_data(config):
    setting = load_config(config)
    email = setting['NOTIFICATION_EMAIL']
    
    try:
        station_data = get_api_data(setting)
        processed_station_data = process_data(station_data,email)
        insert_data_to_db(setting, processed_station_data)
    except Exception as e:
        print(f"Error al obtener o procesar datos de las estaciones: {e}")
        raise

if __name__ == "__main__":
    config_path = 'path_to_your_config_file.json'
    process_station_data(config_path)
