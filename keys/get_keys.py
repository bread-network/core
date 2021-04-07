import json
import os


def get_keys_data():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'keys.json')
    with open(file) as f:
        data = json.load(f)
    return data
