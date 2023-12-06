from scripts.api_client import get_api_data
from scripts.config_loader import load_config
from scripts.data_processor import process_data
from scripts.db_manager import insert_data_to_db


def main(config):
    setting = load_config(config)
    
    try:
        data = get_api_data(setting)
    except Exception as e:
        print(f"Error al obtener datos de la API: {e}")
        return

    processed_data = process_data(data)
    insert_data_to_db(setting, processed_data)

if __name__ == "__main__":
    config = "../config/credentials.json"
    main(config)
