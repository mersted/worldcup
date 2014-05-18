import pymongo
import sys
from datetime import datetime
import calendar

class WorldCup:

    def __init__(self, host="localhost", port=27017):
      self.m = pymongo.MongoClient(host, port)
      self.db = self.m.worldcup

    def insert_game(self, game):
        try:
            self.db.games.insert(game)
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def insert_tweet(self, tweet):
        #change timestamp in tweet to milliseconds
        timedate = tweet['created_at'].split()
        time = "2014-06-" + timedate[2:4]
        date = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        milli = calendar.timegm(date.utctimetuple());
        tweet['created_at'] = milli
        try:
            self.db.tweets.insert(tweet)
        except:
            print("Unexpected error:", sys.exc_info()[0])
