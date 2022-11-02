import time

from jproperties import Properties

from datetime import datetime

from pymongo import MongoClient

p = Properties()
with open("props", "rb") as f:
    p.load(f, "utf-8")
user = p.properties['user']
password = p.properties['password']
database_name = p.properties['database_name']
mongo_string = f'mongodb+srv://{user}:{password}@{database_name}'

cluster = MongoClient(mongo_string)

db = cluster['blazemeter']
collection = db["masterSessions"]

start = datetime(2022, 10, 25, 7, 51, 4)

temp = collection.find({"$and": [{"created": {"$gte": start}}]})
for doc in temp:
    print(doc)
    time.sleep(1)
print('done')
