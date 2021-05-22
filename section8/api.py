import json
import tweepy
with open('./section8/twitter.json') as f:
    twitter_keys = json.load(f)

consumer_key = twitter_keys['consumer_key']
consumer_secret = twitter_keys['consumer_secret']
access_token = twitter_keys['access_token']
access_token_secret = twitter_keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# print(api)
public_tweets = api.home_timeline()
# print(public_tweets)
# for tweet in public_tweets:
#     print(tweet.text)

me = api.me()
# print(me)
# print(me.created_at, me.description)
# print(me.followers_count, me.friends_count)
# print(me.url, me.followers()[0].created_at)
# user = api.get_user('@SMED1374')
# print(user.followers_count)
# print(user.entities)
# print(user.id)
# follower = user.followers()[0]
# print(follower.friends_count)
# api.update_status('テスト投稿です')
# api.update_with_media(status='テスト投稿です', filename='')
# tweet_id = '1394677688430825476'
# api.create_favorite(tweet_id)
# api.retweet(tweet_id)
posts = api.search(q='Python', count=50)
# print(len(posts))
for post in posts:
    tweet_id = post.id
    api.create_favorite(tweet_id)
