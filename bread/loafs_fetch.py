from keys.keys import get_sticks_collection
from bread.constants import LoafConstants


collection = get_sticks_collection()


def get_loaf_names():
    global collection
    loafs = []
    for i in collection.distinct(LoafConstants.LOAF):
        loafs.append(i)
    return loafs