from pymongo import MongoClient
import json
import os

ip = None
port = None
db = None
sticks_coll = None
user_metadata_coll = None
trending_coll = None
username = None
password = None


def get_mongo_creds():
    global ip, port, db, sticks_coll, user_metadata_coll, trending_coll, username, password
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'mongo_keys.json')
    with open(file) as f:
        data = json.load(f)

    ip = data['ip']
    port = data['port']
    db = data['db']
    sticks_coll = data['sticks_coll']
    user_metadata_coll = data['user_metadata_coll']
    trending_coll = data['trending_coll']
    username = data['username']
    password = data['password']


def get_keys_data():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cur_dir, 'keys.json')
    with open(file) as f:
        data = json.load(f)
    return data


def get_mongo_client():
    global ip, db, username, password
    get_mongo_creds()
    try:
        conn = MongoClient(f"mongodb+srv://{username}:{password}@{ip}/{db}")
    except:
        conn = MongoClient(f"mongodb://{username}:{password}@{ip}/{db}")
    db = conn[db]
    return db


def get_sticks_collection():
    global db, sticks_coll
    if db is None:
        db = get_mongo_client()
    coll = db[sticks_coll]
    return coll


def get_user_metadata_collection():
    global db, user_metadata_coll
    if db is None:
        db = get_mongo_client()
    coll = db[user_metadata_coll]
    return coll


def get_trending_collection():
    global db, trending_coll
    if db is None:
        db = get_mongo_client()
    coll = db[trending_coll]
    return coll
