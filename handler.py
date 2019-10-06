import tweepy
from textblob import TextBlob
import os

class Streamer(tweepy.StreamListener):
    
    _sum= 0
    count= 0
    negs = 0
    pos = 0
    neut = 0
    
    def on_status(self, status):
        analysis = TextBlob(status.text)
        polarity = analysis.sentiment.polarity
        noob_analysis(polarity)        
        print_analysis()

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

    def noob_analysis(self, polarity):
        if polarity > 0:
            Streamer.pos += 1
        if polarity == 0:
            Streamer.neut += 1
        if polarity < 0:
            Streamer.negs += 1
        Streamer._sum += polarity
        Streamer.count += 1

    def print_analysis(self):
        print([round(Streamer._sum/ Streamer.count,4),Streamer.pos, Streamer.negs, Streamer.neut])
        
