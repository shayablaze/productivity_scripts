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

start = datetime(2022, 11, 1, 7, 51, 4)

temp = collection.find( {"$and":[{"created": {"$gte":start} }]}  )

tests = []
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
        tests = list(set(tests) | set([doc['test']]))
    elif 'testCollection' in doc:
        # print(doc['test'])
        if doc['testCollection'] not in tests:
            count_tests+=1
        tests = list(set(tests) | set([doc['testCollection']]))
        # print(tests)
    else:
        master_id = doc['_id']
        # print(f'no test wtf with master: {master_id}')
        masters_with_no_test = list(set(masters_with_no_test) | set([doc['_id']]))
        count_master_no_test +=1

print('no tests in these masters')
print(masters_with_no_test)

print('count of tests')
print(count_tests)

print('count of no tests')
print(count_master_no_test)
f.close()
print('done')





