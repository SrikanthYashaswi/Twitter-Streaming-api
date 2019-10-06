import tweepy
from textblob import TextBlob
import os

class Classifier(tweepy.StreamListener):
    
    _sum= 0
    count= 0
    negs = 0
    pos = 0
    neut = 0
    
    def on_status(self, status):
        analysis = TextBlob(status.text)
        polarity = analysis.sentiment.polarity
        self.noob_analysis(polarity)        
        self.print_analysis()
        #self.print_text(status)

    def on_error(self, status_code):
        if status_code == 420:
            print(status_code)
            return False

    def noob_analysis(self, polarity):
        if polarity > 0:
            Classifier.pos += 1
        if polarity == 0:
            Classifier.neut += 1
        if polarity < 0:
            Classifier.negs += 1
        Classifier._sum += polarity
        Classifier.count += 1

    def print_analysis(self):
        avg = round(Classifier._sum/ Classifier.count,4)
        smiley = "..."
        if avg > 0.5:
            smiley = "😃"
        if avg > 0 and avg < 0.5:
            smiley = "🙂"
        if avg == 0:
            smiley = "😐"
        if avg > -0.5 and avg < 0:
            smiley = "🙁"
        if avg < -0.5:
            smiley = "😨"
        print(["exp:",smiley,"+ve: ",Classifier.pos, "-ve:", Classifier.negs,"neut:", Classifier.neut])

    def print_text(self, text):
        print("-->")
        print(text)
        print("<<")

        
