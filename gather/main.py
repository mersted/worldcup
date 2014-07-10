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

    def update_tweet(self, tweet):
        #change timestamp in tweet to milliseconds
        timedate = tweet['created_at'].split()
        time = "2014-06-" + timedate[2] + " " + timedate[3]
        date = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        milli = calendar.timegm(date.utctimetuple())
        try:
            self.db.tweets3.update({'_id' : tweet['_id']}, {'$set' : {'created_at' : milli}})
        except:
            print("Unexpected error:", sys.exc_info()[0])

w = WorldCup()
cursor = w.db.tweets3.find()
for tweet in cursor:
    w.update_tweet(tweet)
