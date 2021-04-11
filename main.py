from flask import Flask, request
from flask_cors import CORS
from bread.twitter_data_fetch import get_profile_tweets
from bread.user_fetch import get_verify_user, get_user_from_username, get_annotation_request
from bread.sticks_fetch import get_loaf_names, get_sticks_of_loaf, get_stick, get_like_stick
from bread.trending_fetch import get_trending
from bread.sticks_update import update_stick_with_annotation
from multiprocessing import Process
import json
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

GET = 'GET'
POST = 'POST'
json_mime = 'application/json'


@app.route('/')
def hello():
    return {'data': 'Welcome to Bread'}


@app.route('/trending', methods=[GET])
def get_trending_sticks():
    if request.method == GET:
        sticks = get_trending()
        random.shuffle(sticks)
        resp = {'sticks': sticks}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/annotation-request/<username>/<loaf>', methods=[GET])
def perform_annotation(username, loaf):
    if request.method == GET:
        anno = get_annotation_request(username, loaf)
        if anno['annotation']:
            return app.response_class(response=json.dumps(anno), status=200, mimetype=json_mime)
        else:
            response = {'annotation': False}
            return app.response_class(response=json.dumps(response), status=200, mimetype=json_mime)


@app.route('/user-annotation/<username>/<stick_id>', methods=[GET])
def user_annotation(username, stick_id):
    if request.method == GET:
        stick = get_stick(stick_id)
        user = get_user_from_username(username)
        myid = user['id']
        for i in stick['annotation']['annotations']:
            if list(i.keys())[0] == str(myid):
                return app.response_class(response=json.dumps({'score': float(i[str(myid)])}), status=200,
                                          mimetype=json_mime)
        return app.response_class(response=json.dumps({'score': None}), status=200, mimetype=json_mime)


@app.route('/verify-user/<username>', methods=[GET])
def verify_user(username):
    if request.method == GET:
        print('here')
        username = get_verify_user(username)
        if username is None:
            resp = {'exists': False}
        else:
            user = get_user_from_username(username)
            resp = {'exists': True, 'profile_image_url_https': user['profile_image_url_https']}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/user/<username>', methods=[GET])
def get_user(username):
    if request.method == GET:
        user = get_user_from_username(username)
        resp = {'user': user}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/stick/<stick_id>', methods=[GET])
def get_my_stick(stick_id):
    if request.method == GET:
        stick = get_stick(stick_id)
        resp = {'stick': stick}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/get-loafs', methods=[GET])
def get_loafs():
    if request.method == GET:
        loaf_names = get_loaf_names()
        resp = {'loafs': loaf_names}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/loafs/<loaf>', methods=[GET])
def get_sticks_of_a_loaf(loaf):
    if request.method == GET:
        sticks = get_sticks_of_loaf(loaf)
        random.shuffle(sticks)
        sticks = sticks[:50]
        resp = {'sticks': sticks,
                'loaf': loaf}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/annotate', methods=[POST])
def annotate_stick():
    if request.method == POST:
        data = request.args
        username = data['username']
        stick_id = int(data['stick_id'])
        score = float(data['score'])
        process = Process(
            target=update_stick_with_annotation,
            args=(username, stick_id, score),
            daemon=True
        )
        process.start()
        resp = {'update': True,
                'username': username,
                'stick_id': stick_id}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/stick/like', methods=[POST])
def like_stick():
    if request.method == POST:
        data = request.args
        stick_id = data['stick_id']
        process = Process(
            target=get_like_stick,
            args=(stick_id, True),
            daemon=True
        )
        process.start()
        resp = {'update': True,
                'stick_id': stick_id}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/stick/dislike', methods=[POST])
def dislike_stick():
    if request.method == POST:
        data = request.args
        stick_id = data['stick_id']
        process = Process(
            target=get_like_stick,
            args=(stick_id, False),
            daemon=True
        )
        process.start()
        resp = {'update': True,
                'stick_id': stick_id}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/profile-tweets', methods=[POST])
def profile_tweets():
    if request.method == POST:
        data = request.args
        username = data['username']
        if 'offset' in data:
            offset = data['offset']
        else:
            offset = 0
        if 'limit' in data:
            limit = data['limit']
        else:
            limit = 5
        tweets = get_profile_tweets(username, limit, offset)
        resp = {'tweets': tweets,
                'username': username}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


if __name__ == '__main__':
    app.run(debug=True)
