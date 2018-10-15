import json
import tweepy
import csv

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

api = tweepy.API(auth)

<<<<<<< HEAD

for i in range(1,20):
    api.update_status("This is automated Tweet #" + str(i));
=======
with open('tweets.csv','rb') as csvfile:
    tweets = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in tweets:
        api.update_status(' '.join(row))
>>>>>>> 8947446373571a214cd0f22a0710dba80d1f16c3
