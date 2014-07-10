World Cup
=========

# Objectives
Analyze Twitter data during 2014 World Cup games

## Analysis
* Look at tweets in the specific countries playing
* Look at both sentiment and frequency
* Use MongoDB and PyMongo for frequency analysis

## Text Search
To search the text in the tweets for specific games,
PyMongo and MongoDB were used.  An index was created on
the 'text' value of tweets.

In the mongo shell: ```db.tweets.ensureIndex({text : "text"})```.

To search for tweets containing a specific word: ```db.tweets.find({'$text' : {'$search' : word}})```

## Performance
A few indexes were added to each collection of tweets in Mongo to improve querying speed

On the 'created_at' field: ```db.tweets.ensureIndex({'created_at' : 1})```

On the 'text' field: ```db.tweets.ensureIndex({'text : 1'})```
