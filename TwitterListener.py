import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from Lab3 import Access


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('ArtificialIntelligenceTweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True



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

print("Begin listening...")

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['ArtificialIntelligence'])