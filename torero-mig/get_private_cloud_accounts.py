from jproperties import Properties
from pymongo import MongoClient
from bson import ObjectId
p = Properties()
with open("props", "rb") as f:
    p.load(f, "utf-8")
user = p.properties['user']
password = p.properties['password']
database_address = 'prod-main.ewwd2.mongodb.net'
database_name = 'payments'
mongo_string2 = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'


cluster = MongoClient(mongo_string2)

db = cluster['payments']
collection = db["plans"]


plans_private_cloud = collection.find( {'planData.privateData':True} )

plans = []
for plan in plans_private_cloud:
    # print(plan['_id'])
    plans.append(ObjectId(plan['_id']))


collection = db["accounts"]
accounts_with_private_cloud = collection.find({"subscriptions.plan" : {"$in": plans}})

i = 1
for acc in accounts_with_private_cloud:
    print(f'{i})')
    print(acc['uid'])
    print(acc['email'])
    print('')
    i+=1