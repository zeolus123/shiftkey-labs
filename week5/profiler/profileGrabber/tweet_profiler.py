import tweepy
import time
from collections import defaultdict


def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"
    return user_profile

def get_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        saved_tweets = []
        tweets = api.user_timeline(screen_name=screen_name, count=10)
        for x in tweets:
            saved_tweets.append(x)

    except:
        print("not working, Can't collect tweets")
    return saved_tweets
