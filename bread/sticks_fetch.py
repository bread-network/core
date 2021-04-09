from keys.keys import get_sticks_collection
from bread.constants import stickConstants


collection = get_sticks_collection()


def get_loaf_names():
    global collection
    loafs = []
    for i in collection.distinct(stickConstants.LOAF):
        loafs.append(i)
    return loafs