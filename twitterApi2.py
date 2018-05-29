from tweepy import OAuthHandler
from tweepy import API
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key=consumer_key,
                    consumer_secret=consumer_secret)
auth.set_access_token(access_token,
                      access_secret)

api = API(auth)

#text content retrieving needs to be automated
text = []
for t in text:
    api.update_status(t)
    time.sleep(300)
