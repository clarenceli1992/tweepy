# -*- coding: utf-8 -*-
#import twitter
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class StdOutListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print(str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True

class TwitterStreamer():
    '''
    streaming bitches!!!
    '''
    def stream_tweets(self, fetched_tweet_filename, hash_tag_list):
        # This handles Twitter Authentication and connection to the twitter streaming api
         listener = StdOutListener()
         auth = OAuthHandler(consumer_key=consumer_key,
                        consumer_secret=consumer_secret)
         auth.set_access_token(key=access_token,
                          token=access_secret)


        stream = Stream(auth, listener)
        stream.filter()
    


consumer_key = 'S1yjoVXjfpMwSHsEJZefQAL4J'
consumer_secret = 'JYjUbXqAHTwKBM3YivElhRLSNSvZYhw136893eRu698prD3WZd'
access_token = '973086578019979265-WnbNqwPt7Te7V9b2FuRgD9rnDY123yv'
access_secret = '1reLeMjzqCcvkaHs6fHL0i0ObhyOEjCxFimgMI1zYAlQK'

if __name__ == '__main__':
    hash_tag_list = []
   
'''    
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)

print(api.VerifyCredentials())
users = api.GetFollowers()
'''