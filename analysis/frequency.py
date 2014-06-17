import pymongo
from datetime import datetime
import calendar
import sys

connection = pymongo.MongoClient("localhost", 27017)

db = connection.worldcup

def total_tweets_interval(start, end):

    starttime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    millistart = calendar.timegm(starttime.utctimetuple())
    endtime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    milliend = calendar.timegm(endtime.utctimetuple())

    query = {'created_at' : {'$gte' : millistart, '$lte' : milliend}}
    try:
      results = db.tweets.find(query)
      total = results.count()
      return total
    except:
      print("Unexpected error:", sys.exc_info()[0])
      return 0



def average_tweets_interval(total, time):
    return total / time

def generate_time_interval(day, month, hour, minute):

    if minute < 55:
        m2 = minute + 5
        h2 = str(hour)
    else:
        m2 = 5 - (60 - minute)
        h2 = str(hour + 1)

    if minute < 10:
        m = "0" + str(minute)
    else:
        m = str(minute)

    if m2 < 10:
        m2 = "0" + str(m2)
    else:
        m2 = str(m2)

    s = str(hour) + ":" + m + ":00"
    e = h2 + ":" + m2 + ":00"

    start = "2014-" + month + "-" + day + " " + s
    end = "2014-" + month + "-" + day + " " + e

    return start, end

def match_time_intervals(day, month, gametime):

    buckets = {}

    hour = int(gametime[:2])
    minute = int(gametime[3:5])

    for m in range(25):
        if minute < 55:
            x, y = generate_time_interval(day, month, hour, minute)
            minute += 5
        else:
            x, y = generate_time_interval(day, month, hour, minute)
            hour += 1
            minute = 5 - (60 - minute)

        tot = total_tweets_interval(x, y)
        buckets[x] = tot

    return buckets

def create_text_file(dict, filename):

    f = open(filename, "w")
    print("Creating text file called ", filename)

    for (interval, total) in dict.items():
        f.write(interval + "\t" + str(total) + "\n")

# function call for first game, Brasil v. Croatia
results = match_time_intervals("12", "06", "19:52:00")
create_text_file(results, "BRAvCRO_2.txt")
# start = 1402602728
