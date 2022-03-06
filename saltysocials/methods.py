import os, time
import openapi
import requests
import tweepy
import configparser
import openai

from .settings import OPENAI_API_KEY, BEARER_TOKEN

# helper for approved_tweets
def is_target_tweet(tweet, keywords):

    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=f"Decide whether a Tweet's sentiment is positive, neutral, or negative. Tweet: {tweet}",
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0,
    presence_penalty=0.0
    )

    sentiment = response['choices'][0]['text']
    print(sentiment)
    return 'negative' in sentiment.strip()

# grabs most recent n tweets; if the tweet contains any of the keywords and the
# sentiment is negative then we add to list of tweets to include on recommendation view
def approved_tweets(keywords):

    retlist = []
    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    for keyword in keywords:
        response = client.search_recent_tweets(query=f"{keyword} -is:retweet", max_results=10)
        if response.data:
            tweets = [tweet.text for tweet in response.data]
            ids = [tweet.id for tweet in response.data]
            print(ids)

            for i in range (0, len(tweets)):
                if is_target_tweet(tweets[i], keywords):
                    retlist.append(ids[i])
                    print(True)
                time.sleep(0.25)

    print(retlist)
    return retlist
