import os
import yaml
import logging

file_path = os.path.join('', os.path.dirname(os.path.abspath(__file__)), 'config', 'config.yaml')

with open(file_path, "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as ex:
        logging.error(f"Error reading yaml file - {ex}.")
