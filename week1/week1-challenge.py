# Week 1 Challenge: build a Tweet Retriever

# Can you create a script that takes a twitter screen_name and returns their
# most recent tweets? You can read more about the Twitter api at https://dev.twitter.com/rest/public

import tweepy
import time


# this is used to collect the twitter names
from collections import defaultdict

# this function collects a twitter profile screen_name and returns their tweets
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        saved_tweets = []
        tweets = api.user_timeline(screen_name=screen_name, count=10)
        print("test1")
        for x in tweets:

            saved_tweets.append(x)
            #print(type(x.user))
        for tweet in saved_tweets:
            print(tweet.id_str)
    except:
        print("Not working")

    return tweets

tweets = get_profile("realDonaldTrump")
