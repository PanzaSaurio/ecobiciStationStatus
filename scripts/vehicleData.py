# vehicleData.py

from scripts.api_client import get_vehicle_position_data
from scripts.config_loader import load_config
from scripts.data_processor import process_vehicle_data_task
from scripts.db_manager import insert_vehicle_data_to_db

def process_vehicle_data(config, route_id=None, agency_id=None):
    setting = load_config(config)
    
    try:
        vehicle_data = get_vehicle_position_data(setting, route_id=route_id, agency_id=agency_id)
        processed_vehicle = process_vehicle_data_task(vehicle_data)
        print(processed_vehicle)
        insert_vehicle_data_to_db(setting, processed_vehicle)
    except Exception as e:
        print(f"Error al obtener o procesar datos de la posición de los vehículos: {e}")
        raise

if __name__ == "__main__":
    config_path = 'path_to_your_config_file.json'
    process_vehicle_data(config_path, agency_id=49) 
