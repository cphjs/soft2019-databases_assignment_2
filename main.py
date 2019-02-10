import pymongo
from pymongo import MongoClient
import re
from bson.code import Code
import time as time_

def millis():
    return int(round(time_.time() * 1000))

def count_distinct(col, attr):
    result = col.aggregate([ 
            { "$group": { '_id': "$user" } },
            { "$group": { 
                    '_id': None, 
                    'count': { "$sum": 1 } 
                } 
            } 
        ])
    return result.next()['count']

def get_most_mentioning(col, attr, limit):
    mm = []
    pattern = re.compile('@\w+')
    for tweet in col.find({ attr: { '$regex': '@\w+' } }):
        matches = pattern.findall(tweet[attr])
        count = len(matches)
        if (count == 0): 
            continue

        if (len(mm) == 0):
            mm.append((tweet['user'], count))
            continue

        # if smaller than last, don't bother
        if (count < mm[len(mm)-1][1]): 
            continue
        
        # if largest ever, insert into start
        if (mm[0][1] < count): 
            mm.insert(0, (tweet['user'], count))
            continue
            
        for i in range (len(mm) - 1, -1, -1):
            if (mm[i][1] > count):
                mm.insert(i + 1, (tweet['user'], count))
                break

        if (len(mm) > limit): 
            mm = mm[:limit]
    return mm

def get_most_mentioned(col, attr, limit):
    mapper = Code("""function() { 
        var matches = this.text.match(/@\w+/g) 
        if (matches) 
            matches.forEach(m => emit(m, 1)) 
        }""")
    reducer = Code("""function(key, values) {
        return Array.sum(values)
    }""")
    result = col.map_reduce(mapper, reducer, { "inline": 1 })
    return sorted(result['results'], key=lambda k: k['value'], reverse=True)[:limit]

def get_most_active(col, attr, limit):
    return col.aggregate([
        { "$group": { 
                "_id": "$user",
                "count": { "$sum":  1},
            }
        },
        { "$sort": { "count": -1 } },
        { "$limit": limit }
    ])

def get_top_polarity(col, polarity, limit):
    #db.tweets_big.aggregate([{ $match: { polarity: { $in: [0, 4] }  }  },  
    # { $group: { _id: { user: '$user', polarity: '$polarity' }, all: { $push: '$polarity' } } }, 
    # {$addFields: { size: { $size: '$all'} } }, { $sort: { 'size': -1 }  }], { allowDiskUse: true})

    # db.tweets_big.aggregate([{ $match: { polarity: { $in: [0, 4] }  }  },  
    # { $group: { _id: { user: '$user', polarity: '$polarity' }, sum: {$sum: 1} } }, 
    # { $sort: { 'sum': -1 }  }], { allowDiskUse: true})
    result = col.aggregate([
        { "$match": { "polarity": polarity } },
        { 
            "$group": 
            {
                "_id": { 'user': '$user', 'polarity': '$polarity'},
                'count': { '$sum': 1 },
            }
        },
        { "$sort": { 'count': -1 } },
        { "$limit": limit },
    ])
    return result


#client = MongoClient("mongodb://172.17.0.2:27017")
#db = client.assignment_2
#tweets = db.tweets_big

client = MongoClient()
db = client.social_net
tweets = db.tweets

start = millis()
print('Distinct users: ' + str(count_distinct(tweets, 'user')))
print('This took ' + str(millis() - start) + ' MS')

print("\nUsers mentioning others the most:")
start = millis()
for user, count in get_most_mentioning(tweets, 'text', 10):
    print(user + ' - ' + str(count) + ' mentions')
print('This took ' + str(millis() - start) + ' MS')

print('\nMost mentioned users')
start = millis()
#for item in get_most_mentioned(tweets, 'text', 5):
#    print(item['_id'] + ' - ' + str(int(item['value'])))
#print('This took ' + str(millis() - start) + ' MS')
print('===============================================')
print('This section was commented out because its slow')
print('===============================================')

print('\nMost active user(by number of tweets)')
start  = millis()
for item in get_most_active(tweets, 'user', 5):
    print(item['_id'] + ' - ' + str(item['count']) + ' tweets')
print('This took ' + str(millis() - start) + ' MS')

print('\nMost grumpy users:')
start = millis()
for item in get_top_polarity(tweets, 0, 5):
    print(item['_id']['user'] + ' - ' + str(item['count']) + ' negative tweets')
print('This took ' + str(millis() - start) + ' MS')

print('\nMost happy users:')
start = millis()
for item in get_top_polarity(tweets, 4, 5):
    print(item['_id']['user'] + ' - ' + str(item['count']) + ' positive tweets')
print('This took ' + str(millis() - start) + ' MS')


client.close()