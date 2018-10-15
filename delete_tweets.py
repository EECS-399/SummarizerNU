import json
import tweepy
import csv

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

api = tweepy.API(auth)

def batch_delete(api):
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print "Deleted:", status.id
            except:
                print "Failed to delete:", status.id

if __name__ == "__main__":
    batch_delete(api)
