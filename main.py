import pymongo

class WorldCup:

    def __init__(self, host="localhost", port=27017):
      self.m = pymongo.MongoClient(host, port)
      self.db = self.m.worldcup

    def insert_game(self, game):
        try:
            self.db.games.insert(game)
        except:
            return
