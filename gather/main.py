import pymongo
import sys

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
        try:
            self.db.tweets.insert(tweet)
        except:
            print("Unexpected error:", sys.exc_info()[0])
