import requests

def get_api_data(config):
    url = f"{config['BASE_URL']}{config['ENDPOINT']}?client_id={config['CLIENT_ID']}&client_secret={config['CLIENT_SECRET']}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error en la respuesta de la API: HTTP {response.status_code}")

    try:
        data = response.json()
    except ValueError:
        raise ValueError("No se pudo decodificar JSON de la respuesta de la API")

    if 'data' not in data or 'stations' not in data['data']:
        raise ValueError("Formato de respuesta de la API inesperado")

    return data
