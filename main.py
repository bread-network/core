from flask import Flask, request
from bread.twitter_data_fetch import get_profile_tweets
from bread.loafs_fetch import get_loaf_names
import json


app = Flask(__name__)
GET = 'GET'
POST = 'POST'
json_mime = 'application/json'


@app.route('/')
def hello():
    return {'data': 'Welcome to Bread'}


@app.route('/get-loafs', methods=[GET])
def get_loafs():
    if request.method == GET:
        loaf_names = get_loaf_names()
        resp = {'loafs': loaf_names}
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


@app.route('/profile_tweets', methods=[POST])
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
        print(resp)
        return app.response_class(response=json.dumps(resp), status=200, mimetype=json_mime)


if __name__ == '__main__':
    app.run(debug=True)
