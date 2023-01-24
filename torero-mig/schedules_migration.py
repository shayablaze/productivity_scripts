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


workspaces_migrated_from_private_cloud = []
orgs_migrated = db['organizations']
query_orgs_migrated = {"$and":[{"migratedFromPc": 'ended' }]}
workspaces_migrated = orgs_migrated.find( query_orgs_migrated )
workspaces_ids_migrated = []
for wm in workspaces_migrated:
    idd = wm['_id']
    workspaces_ids_migrated.append(idd)




workspaces_private_cloud = []
for acc in accounts_from_blazemeter:
    # print(acc['workspaces'])
    # print(acc['name'])
    workspaces_private_cloud = list(set(workspaces_private_cloud) | set(acc['workspaces']))
# print('FROM BLAZEMETER ACCOUNTS HERE are the workspaces')
# print(workspaces_to_exclude)

workspaces_private_cloud = list(filter(lambda x: x not in workspaces_ids_migrated, workspaces_private_cloud))
collection = db['projects']

query = {"$and":[{"workspace": {"$in":workspaces_private_cloud}}]}


projects_from_blaze = collection.find( query )
projects_to_exclude = []

for proj in projects_from_blaze:
    projects_to_exclude.append(proj['_id'])

# print('FROM BLAZEMETER PROJECT to exclude')
# print(projects_to_exclude)
# print(len(projects_to_exclude))


collection = db['tests']

query = {"$and":[{"project": {"$in":projects_to_exclude}}, {"deleted": {"$exists":False }}]}

tests_from_db = collection.find(   query)

print('printing tests')
i = 1
all_test_ids_private_cloud = []
for test in tests_from_db:
    test_id=test['_id']
    # print(f'test id : {i}) {test_id}')
    all_test_ids_private_cloud.append(test_id)
    i+=1
# print('all test ids')
# print(all_test_ids_private_cloud)
# print(f'test array length is {len(all_test_ids_private_cloud)}')

number_of_tests = collection.count_documents(query)
print(f'number of tests is {number_of_tests}')


query = {"$and":[{"test": {"$in":all_test_ids_private_cloud}}, {"deleted": {"$exists":False }}]}
collection_schedules = db['schedules']
schedules_private_cloud = collection_schedules.find(   query)

scheudle_ids_private_cloud = []
print('Printing all schedules private cloud')
for schedule in schedules_private_cloud:
    idd=schedule['_id']
    # print(f'schedule id : {i}) {idd}')
    scheudle_ids_private_cloud.append(idd)
    # all_test_ids_private_cloud.append(test_id)
    i+=1


# number_of_schedulers = collection_schedules.count_documents(query)
print(f'number of scheulders for private cloud is {len(scheudle_ids_private_cloud)}')

## non private cloud

query = {"$and":[{"test": {"$nin":all_test_ids_private_cloud}}, {"deleted": {"$exists":False }}]}
collection_schedules = db['schedules']
schedules_non_private_cloud = collection_schedules.find(   query)

scheudle_ids_non_private_cloud = []
print('Printing all schedules non private cloud')
for schedule in schedules_non_private_cloud:
    idd=schedule['_id']
    # print(f'schedule id : {i}) {idd}')
    scheudle_ids_non_private_cloud.append(idd)
    # all_test_ids_private_cloud.append(test_id)
    i+=1


print(f'number of scheulders for NON private cloud is {len(scheudle_ids_non_private_cloud)}')