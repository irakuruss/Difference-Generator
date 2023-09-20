import os
import json
import yaml


def get_ext(path):
    _, ext = os.path.splitext(path)
    return ext.strip('.')


def parse(data, ext):
    if ext == 'json':
        return json.loads(data)
    elif ext in ('yml', 'yaml'):
        return yaml.load(data, Loader=yaml.Loader)
    else:
        raise ValueError(f'Unsupported data format: {ext}')
