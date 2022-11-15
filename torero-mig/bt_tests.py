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
mongo_string_blaze = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'

cluster = MongoClient(mongo_string_blaze)

db = cluster['blazemeter']
collection = db['accounts']

query = {'_id':{'$in' : [ 40310, 373013, 165479]}}


accounts_from_blazemeter = collection.find( query )


workspaces_to_use = []
for acc in accounts_from_blazemeter:
    print(acc['workspaces'])
    workspaces_to_use = list(set(workspaces_to_use) | set(acc['workspaces']))

collection = db['projects']

query = {"$and":[{"workspace": {"$in":workspaces_to_use}}]}


projects_from_blaze = collection.find( query )
projects_to_use = []

for proj in projects_from_blaze:
    projects_to_use.append(proj['_id'])

# print('FROM BLAZEMETER PROJECT to exclude')
# print(projects_to_exclude)
# print(len(projects_to_exclude))


collection = db['tests']

start = datetime(2022, 5, 8, 7, 1, 1)
end = datetime(2022, 11, 14, 7, 1, 1)
# query = {"$and":[{"project": {"$in":projects_to_use}}, {"deleted": {"$exists":False}}, {"lastRunTime": {"$exists":True}}, { "configuration.type": {"$nin" : [ "functionalGui" ]}    },{"configuration.testMode": {"$nin" : ["http"]}}, {"configuration.scriptType": {"$in" : ["jmeter", "taurus"]}}, {"lastRunTime": {"$gte":start , "$lte":end}}]}
query = {"migratedJmeterVersionsFlag":True}
tests_from_db = collection.find(   query)

print('printing tests')
i = 1
no_jmeter_versions = []
for test in tests_from_db:
    test_name=test['name']
    test_id=test['_id']
    configuration = test['configuration']

    if configuration and 'designatedJmeterVersions' in configuration:
        jmeter_versions =test['configuration']['designatedJmeterVersions']
        print(f'{i}) Name {test_name}. Id: {test_id}: Jmeter versions {jmeter_versions}')
    else:
        no_jmeter_versions.append(test_id)
    i+=1
number_of_tests = collection.count_documents(query)
print(f'number of tests is {number_of_tests}')
print(f'No versions {no_jmeter_versions}')

i=0
for no_jmete in no_jmeter_versions:
    print(f'{i}) {no_jmete}')
    i+=1

print('DONE')