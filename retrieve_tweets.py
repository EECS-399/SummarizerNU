from TwitterSearch import *
import json
import csv
from TwitterSearch import *

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# write = open("searchedTweets.csv", "w")
def searchwords(key):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([key]) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see English tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

<<<<<<< HEAD
<<<<<<< HEAD
api = tweepy.API(auth)

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Trump', 'Cheeseburger']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
=======
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(["New York Giants"]) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
>>>>>>> 41ec331c54a1e65c00537afcf7972092807eb81c
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
<<<<<<< HEAD
        consumer_key = "rA9zDVa3WH2MHJSUqGfBY7cbu",
        consumer_secret = "RoLwp59BpyjS8pkoceYn1T4Lg68lXjIoBs1yzJOLHJxWQMf0ER",
        access_token = "1048307021353836545-bBdvGm2XEsHB5gN4QN6RzmXSohzwGj",
        access_token_secret = "SHcdLpJBuURsT6fRUXs4zaHF6pZ5ZuhDNbj9rRD9aYffL"
     )

     # this is where the fun actually starts :)

=======
        consumer_key = creds['CONSUMER_KEY'],
        consumer_secret = creds['CONSUMER_SECRET'],
        access_token = creds['ACCESS_TOKEN'],
        access_token_secret = creds['ACCESS_SECRET']
     )

     # this is where the fun actually starts :)
>>>>>>> 41ec331c54a1e65c00537afcf7972092807eb81c
    i = 0
    with open("searchedTweets.csv", "w") as file:
        file_writer = csv.writer(file, dialect='excel')
        for tweet in ts.search_tweets_iterable(tso):
            if i < 1000:
                file_writer.writerow([tweet['text'].encode('utf-8').strip()])
<<<<<<< HEAD
                i += 1
=======
                i = i + 1
>>>>>>> 41ec331c54a1e65c00537afcf7972092807eb81c
            else:
                break
=======
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = creds['CONSUMER_KEY'],
            consumer_secret = creds['CONSUMER_SECRET'],
            access_token = creds['ACCESS_TOKEN'],
            access_token_secret = creds['ACCESS_SECRET']
         )

         # this is where the fun actually starts :)
        i = 0
        with open("searchedTweets.csv", "a") as file:
            file_writer = csv.writer(file, dialect='excel')
            for tweet in ts.search_tweets_iterable(tso):
                if i < 1000:
                    file_writer.writerow([tweet['text'].encode('utf-8').strip()])
                    i = i + 1
                else:
                    break

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)
>>>>>>> 2c479a72f53912c9cd25fa1d4af733304980ffab

if __name__ == '__main__':
    word = raw_input("> ")
    searchwords(word)
