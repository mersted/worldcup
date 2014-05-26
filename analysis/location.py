import pymongo
import sys

connection = pymongo.MongoClient("localhost", 27017)

db = connection.worldcup
tweets = db.tweets

def main(xmin, xmax, ymin, ymax):

    query = {}

    try:
        cursor = tweets.find(query)
    except:
        print("Unexpected error:", sys.exc_info()[0])
