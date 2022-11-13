from datetime import datetime

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
account_ids = []
for acc in accounts_with_private_cloud:
    # print(f'{i})')
    # print(acc['uid'])
    # print(acc['email'])
    # print('')
    account_ids.append(  int(acc['uid'].replace('a-', '')))
    i+=1
# print('here are account ids')
# print(account_ids)
#### to blazemeter database

database_name = 'blazemeter'
mongo_string_blaze = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'


cluster = MongoClient(mongo_string_blaze)

db = cluster['blazemeter']
collection = db['accounts']

query = {"$and":[{"_id": {"$in":account_ids} }]}

accounts_from_blazemeter = collection.find( query )


workspaces_to_exclude = []
for acc in accounts_from_blazemeter:
    print(acc['workspaces'])
    workspaces_to_exclude = list(set(workspaces_to_exclude) | set(acc['workspaces']))
# print('FROM BLAZEMETER ACCOUNTS HERE are the workspaces')
# print(workspaces_to_exclude)


collection = db['projects']

query = {"$and":[{"workspace": {"$in":workspaces_to_exclude} }]}


projects_from_blaze = collection.find( query )
projects_to_exclude = []

for proj in projects_from_blaze:
    projects_to_exclude.append(proj['_id'])

# print('FROM BLAZEMETER PROJECT to exclude')
# print(projects_to_exclude)
# print(len(projects_to_exclude))


collection = db['tests']

start = datetime(2022, 5, 8, 7, 1, 1)
end = datetime(2022, 11, 14, 7, 1, 1)
query = {"$and":[{"project": {"$nin":projects_to_exclude}}, {"deleted": {"$exists":False }}, {"lastRunTime": {"$exists":True }}, { "configuration.testMode": {"$nin" : [ "http" ]}    }, { "configuration.scriptType": {"$in" : [ "jmeter", "taurus"  ]}    }, {"lastRunTime": {"$gte":start , "$lte":end } }]}

tests_from_db = collection.find(   query)

# print('printing tests')
# i = 1
# for test in tests_from_db:
#     test_name=test['name']
#     configuration = test['configuration']
#     print(f'test name : {i}) {test_name}')
#     i+=1
number_of_tests = collection.count_documents(query)
print(f'number of tests is {number_of_tests}')
print('DONE')