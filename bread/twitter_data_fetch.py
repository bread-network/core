from keys.keys import get_keys_data
from ..constants import Constants
import tweepy

sample_query = 'Twitter'
en_lang = Constants.LANG
extended_mode = 'extended'


def get_api(offset, cat=1):
    global sample_query, en_lang, extended_mode
    data = get_keys_data()
    i = offset + 1
    while True:
        if i == len(data):
            raise Exception('No More Valid Key Found')
        auth = tweepy.OAuthHandler(data[i]['app_key'], data[i]['app_secret'])
        auth.set_access_token(data[i]['oauth_token'], data[i]['oauth_token_secret'])
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        if api:
            try:
                if cat == 1:
                    api.user_timeline(screen_name='chiragj_', count=1, include_rts=False, tweet_mode='extended')
                elif cat == 2:
                    api.get_status(1374984914836156418)
                return api, i
            except:
                i += 1
        else:
            i += 1


def get_profile_tweets(user_id, limit=5, offset=0):
    all_tweets = []
    oldest_id = offset
    offset = -1
    max_cnt = min(200, limit)
    while len(all_tweets) < limit:
        api, offset = get_api(offset, cat=1)
        if len(all_tweets) == 0:
            tweets = api.user_timeline(screen_name=user_id, count=max_cnt, include_rts=True, tweet_mode='extended')
        else:
            tweets = api.user_timeline(screen_name=user_id, count=max_cnt, include_rts=True, max_id=oldest_id - 1,
                                       tweet_mode='extended')
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        for tweet in tweets:
            all_tweets.append(tweet._json)
    return all_tweets[:limit]
