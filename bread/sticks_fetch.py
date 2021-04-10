from keys.keys import get_sticks_collection
from bread.constants import StickConstants, _id, loaf_image_map, LoafConstants

collection = get_sticks_collection()


def get_loaf_names():
    global collection
    loafs = []
    for i in collection.distinct(StickConstants.LOAF):
        temp = {LoafConstants.NAME: i, LoafConstants.IMAGE: loaf_image_map[i]}
        loafs.append(temp)
    return loafs


def get_sticks_of_loaf(loaf):
    global collection
    sticks = []
    for i in collection.find({StickConstants.LOAF: loaf}, {_id: 0}):
        sticks.append(i)
    return sticks


def get_stick(stick_id):
    global collection
    my_stick = None
    for i in collection.find({StickConstants.ID: stick_id}, {_id: 0}):
        my_stick = i
        break
    return my_stick
