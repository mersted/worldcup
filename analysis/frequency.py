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

def keyword_tweets_total(words):

    buckets_tot = {}
    for word in words:
        query = {'$text' : {'$search' : word}}
        try:
          results = db.tweets2.find(query)
          total = results.count()
          buckets_tot[word] = total
        except:
          print("Unexpected error:", sys.exc_info()[0])

    return buckets_tot

def keyword_tweets_interval(start, end, word):

    starttime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    millistart = calendar.timegm(starttime.utctimetuple())
    endtime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    milliend = calendar.timegm(endtime.utctimetuple())

    query = {'created_at' : {'$gte' : millistart, '$lte' : milliend}, '$text' : {'$search' : word}}
    try:
      results = db.tweets2.find(query)
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
        h2 = hour
    else:
        m2 = 5 - (60 - minute)
        if hour < 23:
            h2 = hour + 1
        else:
            h2 = 0

    if hour < 10:
        h = "0" + str(hour)
    else:
        h = str(hour)

    if h2 < 10:
        h2 = "0" + str(h2)
    else:
        h2 = str(h2)

    if minute < 10:
        m = "0" + str(minute)
    else:
        m = str(minute)

    if m2 < 10:
        m2 = "0" + str(m2)
    else:
        m2 = str(m2)

    s = h + ":" + m + ":00"
    e = h2 + ":" + m2 + ":00"

    start = "2014-" + month + "-" + day + " " + s
    end = "2014-" + month + "-" + day + " " + e

    return start, end

def match_time_intervals(day, month, gametime, words):

    buckets_int = {}

    for word in words:
        hour = int(gametime[:2])
        minute = int(gametime[3:5])
        for m in range(15):
            if minute < 55:
                x, y = generate_time_interval(day, month, hour, minute)
                minute += 5
            else:
                x, y = generate_time_interval(day, month, hour, minute)
                if hour < 23:
                    hour += 1
                else:
                    hour = 0
                minute = 5 - (60 - minute)

            tot = keyword_tweets_interval(x, y, word)
            if word in buckets_int:
              buckets_int[word][x] = tot
            else:
              buckets_int[word] = {x:tot}

    return buckets_int

def create_text_file(data, filename):

    f = open(filename, "w")
    print("Creating text file called ", filename)

    # for (word, tot) in data.items():
    #     f.write(word + "\t" + str(tot) + "\n")

    for (word, x) in data.items():
        f.write(word + ":\n")
        for (interval, total) in x.items():
            f.write(interval + "\t" + str(total) + "\n")

words = ["dempsey", "goal", "brooks", "ayew", "ghana", "usa", "bradley", "gyan", "howard"]
results = match_time_intervals("16", "06", "22:52:00", words)
create_text_file(results, "USAvGHA_2.txt")

# words = ["dempsey", "usa", "goal", "belgium", "lukaku", "howard", "bruyne"]
# results = keyword_tweets_total(words)
# create_text_file(results, "USAvBEL.txt")
#results = match_time_intervals("12", "06", "19:52:00")
#create_text_file(results, "BRAvCRO_3.txt")
# function calls for first USA game, USA v. Ghana
#results = match_time_intervals("16", "06", "22:52:00")
#create_text_file(results, "USAvGHA.txt")
