var mongojs = require('mongojs');
var db = mongojs('worldcup', ['tweets, tweets2, tweets3', 'tweets4', 'tweets5']);

var mostTZ = db.runCommand({aggregate : 'tweets', explain: false, pipeline : [
	{'$match' : {"location.user_timezone" : {'$ne' : null}}},
	{'$group' : {_id : "$location.user_timezone", total : {'$sum' : 1}}},
	{'$sort' : {total : -1}}
	]);