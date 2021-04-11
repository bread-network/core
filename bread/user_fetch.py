from bread.constants import UserConstants, _id
from keys.keys import get_user_metadata_collection
from bread.sticks_fetch import get_sticks_of_loaf
import random
collection = get_user_metadata_collection()


def get_verify_user(username):
    global collection
    my_user = None
    for i in collection.find({UserConstants.USERNAME: username}, {UserConstants.USERNAME: 1}):
        my_user = i[UserConstants.USERNAME]
        break
    return my_user


def get_user_from_username(username):
    global collection
    my_user = None
    for i in collection.find({UserConstants.USERNAME: username}, {_id: 0}):
        my_user = i
        break
    return my_user


def get_annotation_request(username,loaf):
    global collection
    for i in collection.find({UserConstants.USERNAME: username}, {_id: 0}):
        my_user = i
        break
    
    cred = my_user['annotation']['credibility_score']
    annotations = my_user['annotation']['annotations']
    print(cred/len(annotations))
    if cred/len(annotations) > 0.6:
        breads = get_sticks_of_loaf(loaf)
        return {'annotation':True,'bread':random.choice(breads)}
    else:
        return {'annotation':False}



