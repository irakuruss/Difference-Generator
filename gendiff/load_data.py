import json
import yaml
import os


def load_data(path):
    _, ext = os.path.splitext(path)
    with open(path, 'r') as file:
        if ext == '.json':
            data = json.load(file)
        elif ext in ['.yml', '.yaml']:
            data = yaml.safe_load(file)
        else:
            raise ValueError(f'Unsupported file format: {ext}')
        return data
