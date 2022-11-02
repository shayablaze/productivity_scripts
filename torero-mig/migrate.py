import time
import os
from jproperties import Properties

from datetime import datetime

from pymongo import MongoClient
from os.path import exists
p = Properties()
with open("props", "rb") as f:
    p.load(f, "utf-8")
user = p.properties['user']
password = p.properties['password']
database_name =  p.properties['database_name']
mongo_string = f'mongodb+srv://{user}:{password}@{database_name}'

cluster = MongoClient(mongo_string)

db = cluster['blazemeter']
collection = db["masterSessions"]

start = datetime(2022, 11, 2, 7, 51, 4)

temp = collection.find( {"$and":[{"created": {"$gte":start} }]}  )

tests = []
multi_tests = []
masters_with_no_test = []

file_name = 'tests_to_migrate_list.txt'
if exists(file_name):
    os.remove(file_name)
f = open(file_name, "a")
count_tests = 0
count_master_no_test = 0
for doc in temp:
    if 'test' in doc:
        # print(doc['test'])
        if doc['test'] not in tests:
            count_tests+=1
            f.write(f'{doc["test"]}, ')
        tests = list(set(tests) | set([doc['test']]))
    elif 'testCollection' in doc:
        # print(doc['test'])

        if doc['testCollection'] not in multi_tests:
            count_tests+=1
        multi_tests = list(set(multi_tests) | set([doc['testCollection']]))
        # print(tests)
    else:
        master_id = doc['_id']
        # print(f'no test wtf with master: {master_id}')
        masters_with_no_test = list(set(masters_with_no_test) | set([doc['_id']]))
        count_master_no_test +=1

print('here are multi tests')
print(multi_tests)

collection = db["testCollections"]


temp = collection.find( {"$and":[{"_id": {"$in":multi_tests} }]}  )
print('here are the test collections from db')

print('tests before')
print(len(tests))
for doc in temp:
    single_tests_from_multi_test = list(map(lambda x: x['testId'], doc['testsForExecutions']))
    tests = list(set(tests) | set(single_tests_from_multi_test))
print('tests after')
print(len(tests))
    # print(doc)

# print('no tests in these masters')
# print(masters_with_no_test)
#
# print('count of tests')
# print(count_tests)
#
# print('count of no tests')
# print(count_master_no_test)
f.close()
print('done')





