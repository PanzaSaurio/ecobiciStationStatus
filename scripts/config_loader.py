#config_loader.py

import json

def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)
