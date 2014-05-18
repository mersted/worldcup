import pymongo

class WorldCup:

    def __init__(self, host="localhost", port=27017):
      self.m = pymongo.MongoClient(host, port)
      self.db = self.m.worldcup

    def insert_game(self, game):
      try:
        self.db.games.insert(game)
        doc = {
              'home_team' : game['ht'],
              'away_team' : game['at'],
              'stats' : {
                  'home_goals' : game['hg'],
                  'away_goals' : game['ag'],
                  'home_yellow' : game['hy'],
                  'away_yellow' : game['ay'],
                  'home_red' : game['hr'],
                  'away_red' : game['ar']
              },
              'stadium' : game['stadium'],
              'round' : game['round']
              }
