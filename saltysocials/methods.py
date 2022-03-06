import os
import openapi
import requests
import tweepy
import configparser

from .settings import OPENAI_API_KEY

# helper for approved_tweets
def bad_tweet(tweet, keywords):
    tweet = tweet.get('text')

    for keyword in keywords:
        if keyword in tweet:
            return False

    return True

# grabs most recent n tweets; if the tweet contains any of the keywords, we do not append to
# list of approved tweets
def approved_tweets(keywords):

    retlist = []

    # read config
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']

    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    # authentication
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.home_timeline()

    for tweet in tweets:
        if not bad_tweet(tweet, keywords):
            retlist.append(tweet)
