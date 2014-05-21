import pymongo
from datetime import datetime
import calendar
import sys

buckets = {}

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

def average_tweets_interval(total, time):
    return total / time

def generate_time_interval(day, month, hour, minute):

    h = str(hour)
    m = str(minute)
    if minute < 59:
        m2 = str(minute + 1)
        h2 = str(hour)
    else:
        m2 = "00"
        h2 = str(hour + 1)

    s = h + ":" + m + ":00"
    e = h2 + ":" + m2 + ":00"

    start = "2014-" + month + "-" + day + " " + s
    end = "2014-" + month + "-" + day + " " + e

    return start, end

def match_time_intervals(day, month, gametime):
    hour = int(gametime[:2])
    minute = int(gametime[3:5])
    for m in range(150):
        if minute < 59:
            x, y = generate_time_interval(day, month, hour, minute)
            minute += 1
        else:
            x, y = generate_time_interval(day, month, hour, minute)
            hour += 1
            minute = 0

        tot = total_tweets_interval(x, y)
        buckets[x] = tot

# function call for first game, Brasil v. Croatia
match_time_intervals("12", "6", "17:00:00")
