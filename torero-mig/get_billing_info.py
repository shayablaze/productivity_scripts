from jproperties import Properties
from pymongo import MongoClient

p = Properties()
with open("props", "rb") as f:
    p.load(f, "utf-8")
user = p.properties['user']
password = p.properties['password']
database_name =  'prod-main.ewwd2.mongodb.net/payments'
database_address = 'prod-main.ewwd2.mongodb.net'
database_name = 'payments'
mongo_string2 = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'


cluster = MongoClient(mongo_string2)

db = cluster['payments']
collection = db["accounts"]

temp = collection.find( {"$and":[{"uid": 'a-773774' }]}  )

for doc in temp:
    print(doc['email'])

