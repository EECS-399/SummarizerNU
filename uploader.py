import json
import tweepy
import csv

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

api = tweepy.API(auth)

with open('tweets.csv','rb') as csvfile:
    tweets = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in tweets:
        api.update_status(' '.join(row))
