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
PyMongo and MongoDB were used.  An index was created for each
collection of tweets representing a game.

In the mongo shell: ```db.tweets.ensureIndex({text : "text"})```.
