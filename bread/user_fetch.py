from bread.constants import UserConstants
from keys.keys import get_user_metadata_collection


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
    for i in collection.find({UserConstants.USERNAME: username}, ):
        my_user = i
        break
    return my_user
