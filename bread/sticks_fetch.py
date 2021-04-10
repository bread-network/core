from keys.keys import get_sticks_collection
from bread.constants import StickConstants


collection = get_sticks_collection()


def get_loaf_names():
    global collection
    loafs = []
    for i in collection.distinct(StickConstants.LOAF):
        loafs.append(i)
    return loafs