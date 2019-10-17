import json
from datetime import datetime
with open ('twitter.json') as file:
    data = json.load(file, ident=4)

trump = {}

data.sort( key = lambda x: datetime.strptime(x['created_at'], '%a %b %d %X %z %Y'), reverse=True)

print("Length:", len(data))
#print(data[0:4])

test = [ (i['text'], i['retweet_count']) for i in data if i['favorite_count'] > 10000]

print(test)
print(len(test))
test.sort(key = lambda tup: tup[1], reverse=True)

print(test[0:5:1])



test.sort(key = lambda tup: min(tup[0]), reverse=True)

print(test[0][0])