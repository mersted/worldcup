import pymongo
from datetime import datetime
import calendar
import sys

connection = pymongo.MongoClient("localhost", 27017)

db = connection.worldcup
tweets = db.tweets

def interval(start, end):

    starttime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    millistart = calendar.timegm(starttime.utctimetuple())
    endtime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    milliend = calendar.timegm(endtime.utctimetuple())

    query = {'created_at' : {$gte : millistart, $lte : milliend}}
    try:
      total = tweets.count(query)
    except:
      print("Unexpected error:", sys.exc_info()[0])

    return total
