import tweepy
from textblob import TextBlob
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#sentiment analysis
search = 'Penn State'

public_tweets =  api.search(q = search, lang = 'en', locale = 'en', rpp = 10, show_user = 'true')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print("JOE'S ANALYSIS: ")
    print(analysis.sentiment)
