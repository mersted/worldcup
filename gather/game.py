from main import WorldCup

game = {}

#get game data

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

w = WorldCup()

w.insert_game(doc)
