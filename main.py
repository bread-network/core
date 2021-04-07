from flask import Flask, request
from bread.twitter_data_fetch import get_profile_tweets
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return {'data': 'Welcome to Bread'}


@app.route('/profile_tweets', methods=['POST'])
def profile_tweets():
    if request.method == 'POST':
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
        return app.response_class(response=json.dumps(resp), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
