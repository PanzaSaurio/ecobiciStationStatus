import json
import pandas as pd
import requests

def unix_to_readable(unix_timestamp):
    return pd.to_datetime(unix_timestamp, unit='s').strftime('%Y-%m-%d %H:%M:%S')

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

client_id = credentials['CLIENT_ID']
client_secret = credentials['CLIENT_SECRET']

url = f"https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus?client_id={client_id}&client_secret={client_secret}"

response = requests.get(url)
data = response.json()

for station in data['data']['stations']:
    if 'last_reported' in station:
        station['last_reported'] = unix_to_readable(station['last_reported'])


df = pd.DataFrame(data['data']['stations'])

print(f"Cantidad de registros recuperados: {len(df)}")

print(df) 
