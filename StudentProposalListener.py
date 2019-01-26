# This script is based on yanofsky's script.
# https://gist.github.com/yanofsky/5436496

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import json
from Lab3 import Access


#Instance Access object and follow the PIN process
access = Access.obj

#Consumer credentials
consumer_key = access.consumer_key
consumer_secret = access.consumer_secret
#Get the Access Token and the Secret Token from the access OBJ
access_token = access.atk
access_secret = access.ats

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)





#User name:
screen_name='@marianorajoy'

# initialize a list to hold all the tweepy Tweets
alltweets = []

# make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name=screen_name, count=200)

# save most recent tweets
alltweets.extend(new_tweets)

# save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

# keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    # all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    print("...%s tweets downloaded so far" % (len(alltweets)))

# write tweet objects to JSON
with open('tweet.json', 'w') as outfile:
    for status in alltweets:
        json.dump(status._json, outfile)
        # IMPORTANT: write line break in order to avoid python to crash when read
        outfile.write('\n')

print("Done")




