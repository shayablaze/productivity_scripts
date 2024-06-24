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
collection = db["accounts"]

temp = collection.find( {"$and":[{"uid": {'$in':['a-773774', 'a-1344923', 'a-1345158' ]} }]}  )
plan_info = {}
for doc in temp:
    plan = list( map( lambda x: str(x['plan']), list(filter(lambda x : x['canceled'] == False , doc['subscriptions']))))[0]

    if plan not in plan_info:
        plan_info[plan] = []
    plan_info[plan] += [doc['uid']]

subscriptions_in_object_id = list(map(lambda x:ObjectId(x), list(plan_info.keys())))
subscriptions_to_private_cloud = []
collection = db["plans"]

# temp = collection.find( {"$and":[{"_id": {'$in':subscriptions_in_object_id} }]}  )
temp = collection.find( {"$and":[{"_id": {'$in':subscriptions_in_object_id} }]}  )

print('good stuff')
for doc in temp:
    print(doc['planData']['privateData'])
    # subscription_info[doc['uid']] = subscriptions_list_string
print(plan_info)
