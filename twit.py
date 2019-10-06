import tweepy
import json
from textblob import TextBlob
from handler import Streamer

# A wrapper around tweepy
# a collection class that exposes tweepy's most methods.

class Classifier():

    def __init__(self):
        props_file = open("properties.json", "r").read()
        props = json.loads(props_file)
        auth = tweepy.OAuthHandler(props["consumer_key"], props["consumer_secret"])
        auth.set_access_token(props["access_token"], props["access_token_secret"])
        self.api = tweepy.API(auth)

    # topic should be csv of interested topics
    # like topic=["microsoft", "yesbank"]
    
    def track(self, topic):
        s = Streamer()
        myStream = tweepy.Stream(auth = self.api.auth, listener=s)
        myStream.filter(track=topic)
    
    # location  
    # eg: bombay= [72.5740065374,16.8873369378,75.7902342258,21.7017731081]
    # Online-Tool to create boxes http://boundingbox.klokantech.com/ ( bottom left change to csv )
    def track_location(self, location):
        s = Streamer()
        myStream = tweepy.Stream(auth = self.api.auth, listener=s)
        myStream.filter(locations=location)

    # get a list of current trending items around the world
    def trending(self):
        trends = self.api.trends_place(1)    
        print(json.dumps(trends, indent=2))
    
    def indepth(self,subject,items):
        search_hashtag = tweepy.Cursor(self.api.search, q=subject).items(items)
        for tweet in search_hashtag:
            print(json.dumps(tweet._json,indent=2))