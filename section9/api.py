
import os
import requests
from dotenv import load_dotenv
import tweepy

load_dotenv()


def notify_message(message):
    LINE_NOTIFY_TOKEN = os.environ['LINE_NOTIFY_TOKEN']

    url = 'https://notify-api.line.me/api/notify'

    # message = 'これはテストメッセージです'
    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }
    data = {
        'message': message
    }
    requests.post(
        url,
        headers=headers,
        data=data
    )


# message = '関数を用いたテスト通知'
# notify_message(message)

def get_n_followers():
    consumer_key = os.environ['TWITTER_API_KEY']
    consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    me = api.me()
    n_followers = me.followers_count
    return n_followers


n_followers = get_n_followers()
message = f'本日のフォロワー数は{n_followers}です'
notify_message(message)
