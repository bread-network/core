from keys.keys import get_trending_collection
from bread.constants import _id

collection = get_trending_collection()


def get_trending():
    global collection
    sticks = []
    for i in collection.find({}, {_id: 0}):
        sticks.append(i)
    return sticks
