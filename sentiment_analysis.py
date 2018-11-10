import tweepy
from textblob import TextBlob
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#sentiment analysis
q = 'Penn State'
lang = 'en'
locale = 'en'
rpp = 10
page = 1
since_id = 0
geocode = 
show_user = 'true'

public_tweets =  api.search(q, lang, locale, rpp, page, since_id, geocode, show_user)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print("JOE'S ANALYSIS")
    print(analysis.sentiment)
