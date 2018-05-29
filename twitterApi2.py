from tweepy import OAuthHandler
from tweepy import API
import time

consumer_key = 'S1yjoVXjfpMwSHsEJZefQAL4J'
consumer_secret = 'JYjUbXqAHTwKBM3YivElhRLSNSvZYhw136893eRu698prD3WZd'
access_token = '973086578019979265-WnbNqwPt7Te7V9b2FuRgD9rnDY123yv'
access_secret = '1reLeMjzqCcvkaHs6fHL0i0ObhyOEjCxFimgMI1zYAlQK'

auth = OAuthHandler(consumer_key=consumer_key,
                    consumer_secret=consumer_secret)
auth.set_access_token(access_token,
                      access_secret)

api = API(auth)
text = ['This week the two popular #BitcoinCash social media applications, #Memo and #Blockpress have rolled out a bunch of new features on each platform. Now users on both platforms can upload pictures, video, and even torrent magnets found on the Pirate Bay.https://news.bitcoin.com/bch-powered-social-media-apps-launch-new-features/',
        '#Bitmain co-founder Wu Jihan has revealed that his company has huge expansion plans for its #Bitcoin mining operations in the #US during an interview with @Bloomberg. https://btcmanager.com/bitmains-jihan-wu-we-have-really-huge-expansion-plans-for-u-s/']

for t in text:
    api.update_status(t)
    time.sleep(300)