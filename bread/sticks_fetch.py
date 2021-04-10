from keys.keys import get_sticks_collection
from bread.constants import StickConstants, _id

collection = get_sticks_collection()


def get_loaf_names():
    global collection
    loafs = []
    for i in collection.distinct(StickConstants.LOAF):
        loafs.append(i)
    return loafs


def get_sticks_of_loaf(loaf):
    global collection
    sticks = []
    for i in collection.find({StickConstants.LOAF: loaf}, {_id: 0}):
        sticks.append(i)
    return sticks
