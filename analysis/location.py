import pymongo
import sys

connection = pymongo.MongoClient("localhost", 27017)

db = connection.worldcup
tweets = db.tweets

def tweets_by_country(country):

    arr = countries[country]
    xmin = arr[0]
    xmax = arr[1]
    ymin = arr[2]
    ymax = arr[3]

    query = {'location.x' : {'$gte' : xmin, '$lte' : xmax},
              'location.y' : {'$gte' : ymin, '$lte' : ymax}}

    try:
        total = tweets.count(query)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    return total

# dictionary of countries with max and min
# longitude and latitude
countries = {}
# countries['Brazil'] = [xmin, xmax, ymin, ymax]
# countries['Croatia'] = [xmin, xmax, ymin, ymax]

result = tweets_by_country('Brazil')
