import pymongo
from datetime import datetime
import calendar
import sys

connection = pymongo.MongoClient("localhost", 27017)

db = connection.worldcup
tweets = db.tweets

def total_tweets_interval(start, end):

    starttime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    millistart = calendar.timegm(starttime.utctimetuple())
    endtime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    milliend = calendar.timegm(endtime.utctimetuple())

    query = {'created_at' : {'$gte' : millistart, '$lte' : milliend}}
    try:
      total = tweets.count(query)
    except:
      print("Unexpected error:", sys.exc_info()[0])

    return total

def generate_time_interval(day, month, gametime):

    starthour = int(gametime[:2])
    if starthour < 22:
        endhour = starthour + 2
    else:
        endhour = 24 - starthour

    startminute = int(gametime[3:5])
    if startminute < 30:
        endminute = startminute + 30
    else:
        endhour += 1
        endminute = 30 - (60 - startminute)

    endgametime = str(endhour) + ":" + str(endminute) + ":" + gametime[6:]

    start = "2014-" + month + "-" + day + " " + gametime
    end = "2014-" + month + "-" + day + " " + endgametime

    return start, end

# function calls for first game, Brasil v. Croatia
# would calculate total tweets throughout game
x, y = generate_time_interval("12", "6", "17:00:00")
tot = total_tweets_interval(x, y)
