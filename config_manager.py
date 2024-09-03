import yaml
import json

def get_telegram_config():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config['telegram']

def get_database_config():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config['database']