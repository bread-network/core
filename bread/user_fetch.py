from bread.constants import UserConstants
from keys.keys import get_user_metadata_collection


collection = get_user_metadata_collection()


def get_verify_user(username):
    global collection
    my_user = None
    for i in collection.find({UserConstants.USERNAME: username}, {UserConstants.USERNAME: 1}):
        my_user = i[UserConstants.USERNAME]
    return my_user
