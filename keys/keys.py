from pymongo import MongoClient
import json
import os

db = None
ip = None
port = None
db = None
twitter_coll = None
username = None
password = None

def get_mongo_creds():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'mongo_keys.json')
    with open(file) as f:
        data = json.load(f)
    return data['ip'], data['port'], data['db'], data['twitter_coll'], data['username'], data['password']


def get_keys_data():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'keys.json')
    with open(file) as f:
        data = json.load(f)
    return data


def get_mongo_client():
    global ip, port, db, twitter_coll, username, password
    ip, port, db, twitter_coll, username, password = get_mongo_creds()
    conn = MongoClient(f"mongodb+srv://{username}:{password}@{ip}/{db}")
    db = conn[db]
    return db


def get_twitter_collection():
    global db, twitter_coll
    if db is None:
        db = get_mongo_client()
    coll = db[twitter_coll]
    return coll
