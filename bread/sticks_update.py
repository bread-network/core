from keys.keys import get_sticks_collection, get_user_metadata_collection
from bread.constants import StickConstants, _id, UserConstants
from bread.user_fetch import get_user_from_username
from bread.sticks_fetch import get_stick
from datetime import datetime
collection = get_sticks_collection()
bakers = get_user_metadata_collection()


def update_stick_with_annotation(username, stick_id, score):
    # TODO: Implement stick annotation
    # username -> str, stick_id -> int, score -> float
    user = get_user_from_username(username)
    new_entry = {str(user['id']):float(score)}
    collection.update({StickConstants.ID: int(stick_id)}, {'$push': {'annotation.annotations': new_entry}})
    bread = get_stick(stick_id)

    new_polarity_score = (0.6*bread['annotation']['modelPolarityScore'] + 0.4*sum([list(x.values())[0] for x in bread['annotation']['annotations']])/3)
    collection.update({StickConstants.ID: int(stick_id)}, {'$set': {'annotation.polarity_score': new_polarity_score}})

    bakers.update({UserConstants.ID: int(user['id'])}, {'$push': {'annotation.annotations': {str(stick_id):str(datetime.now())}}})






    
    pass
