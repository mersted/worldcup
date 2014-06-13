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
      return total
    except:
      print("Unexpected error:", sys.exc_info()[0])



def average_tweets_interval(total, time):
    return total / time

def generate_time_interval(day, month, hour, minute):

    if minute < 59:
        m2 = minute + 1
        h2 = str(hour)
    else:
        m2 = 0
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

    for m in range(140):
        if minute < 59:
            x, y = generate_time_interval(day, month, hour, minute)
            minute += 1
        else:
            x, y = generate_time_interval(day, month, hour, minute)
            hour += 1
            minute = 0

        tot = total_tweets_interval(x, y)
        buckets[x] = tot

    return buckets

def create_text_file(dict, filename):

    f = open(filename, "w")
    print("Creating text file called ", filename)

    for (interval, total) in dict.items():
        f.write(interval + "\t" + str(total) + "\n")

# function call for first game, Brasil v. Croatia
results = match_time_intervals("12", "06", "20:00:00")
create_text_file(results, "BRAvCRO.txt")
# start = 1402602728
