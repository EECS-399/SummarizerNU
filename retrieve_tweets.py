import json
import tweepy
import csv
from TwitterSearch import *

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

api = tweepy.API(auth)

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Trump', 'Cheeseburger']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = "rA9zDVa3WH2MHJSUqGfBY7cbu",
        consumer_secret = "RoLwp59BpyjS8pkoceYn1T4Lg68lXjIoBs1yzJOLHJxWQMf0ER",
        access_token = "1048307021353836545-bBdvGm2XEsHB5gN4QN6RzmXSohzwGj",
        access_token_secret = "SHcdLpJBuURsT6fRUXs4zaHF6pZ5ZuhDNbj9rRD9aYffL"
     )

     # this is where the fun actually starts :)

    i = 0
    with open("searchedTweets.csv", "w") as file:
        file_writer = csv.writer(file, dialect='excel')
        for tweet in ts.search_tweets_iterable(tso):
            if i < 1000:
                file_writer.writerow([tweet['text'].encode('utf-8').strip()])
                i += 1
            else:
                break

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
