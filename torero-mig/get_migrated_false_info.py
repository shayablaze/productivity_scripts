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
database_name = 'blazemeter'
mongo_string2 = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'



cluster = MongoClient(mongo_string2)

db = cluster['blazemeter']
collection = db["tests"]

tests_migrate_false = collection.find( {'migratedJmeterVersionsFlag':False} )

i =0
projects = []
for test in tests_migrate_false:
    i+=1
    test_name = test['name']
    project = test['project']
    # print(f'{i} ) {test_name}')
    projects = list(set(projects) | set([project]))
# print(projects)

collection = db["projects"]


projects = collection.find( {'_id': {'$in': projects}} )

workspaces_ids = []
for proj in projects:
    workspaces_ids = list(set(workspaces_ids) | set([proj['workspace']]))


query = {"$and":[{"_id": {"$in":workspaces_ids}}]}
collection = db["organizations"]
workspaces = collection.find(query)

users_ids = []
for w in workspaces:
    users_ids = list(set(users_ids) | set([w['userId']]))
# print('users are')
# print(users)

query = {"$and":[{"_id": {"$in":users_ids}}]}
collection = db["users"]
users = collection.find(query)

print('printing users')
i = 1
for u in users:
    email = u['email']
    print(f'{i} ) {email}')
    i+=1

#######

query = {"$and":[{"workspaces": {"$in":workspaces_ids}}]}
collection = db["accounts"]
accounts_from_blazemeter = collection.find(query)
#
print('accounts')
i=1
for acc in accounts_from_blazemeter:
    account_name = acc['name']
    account_id= acc['_id']
    print(f'{i} ) Account name: {account_name}. Account Id: {account_id}')
    i+=1
print('finished printing accounts')







