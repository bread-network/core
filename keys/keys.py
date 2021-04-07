import json
import os


def get_mongo_creds():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'mongo_keys.json')
    with open(file) as f:
        data = json.load(f)
    return data['ip'], data['port'], data['db'], data['username'], data['password']


def get_keys_data():
    get_mongo_creds()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'keys.json')
    with open(file) as f:
        data = json.load(f)
    return data
