import os
import json
import logging

def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error(f"Config file not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse config file: {e}")
        return {}

def write_config(config, file_path):
    try:
        with open(file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)
    except Exception as e:
        logging.error(f"Failed to write config file: {e}")

def get_terraform_version():
    try:
        output = os.popen('terraform --version').read()
        return output.split()[1]
    except Exception as e:
        logging.error(f"Failed to get Terraform version: {e}")
        return None

def get_current_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_project_root():
    current_dir = get_current_dir()
    while True:
        if os.path.exists(os.path.join(current_dir, 'infra-terraform')):
            return current_dir
        if current_dir == '/':
            break
        current_dir = os.path.dirname(current_dir)
    return None