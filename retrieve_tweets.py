from TwitterSearch import *
import json
import csv

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# write = open("searchedTweets.csv", "w")
def searchwords(key):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([key]) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see English tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

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

if __name__ == '__main__':
    word = raw_input("> ")
    searchwords(word)
