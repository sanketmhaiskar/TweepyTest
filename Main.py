from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import io

from Credentials import *
from Sentiment import *

sobj = loaddata()
sobj.loadDictionary()




class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet= str(all_data["text"])
        #print (type (tweet))
        with open("D://foo.txt", "a+") as outfile:
            json.dump(all_data,outfile)
            outfile.write('\n\n')
        print tweet.encode('utf-8',errors='ignore')
        print sobj.calculateSentiment(tweet.split())
        time.sleep(2)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy","sad","excited","angry"],async=True)
