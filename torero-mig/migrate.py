import time
import os
from jproperties import Properties

from datetime import datetime

from pymongo import MongoClient
from os.path import exists


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("before time =", current_time)


p = Properties()
with open("props", "rb") as f:
    p.load(f, "utf-8")
user = p.properties['user']
password = p.properties['password']
database_address =  p.properties['database_address']
database_name = 'blazemeter'


mongo_string = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'

cluster = MongoClient(mongo_string)

db = cluster['blazemeter']
collection = db["masterSessions"]

start = datetime(2022, 11, 3, 5, 51, 4)

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
print('before iterating results')
i = 1

print('calculating count for test')
number_of_documents = collection.count_documents({"$and":[{"created": {"$gte":start} }]})
print(f'we got {number_of_documents} masters')

if number_of_documents == 0:
    print('good bye')
    exit()

for doc in temp:

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    # print(f'in test iteration {i} out of {number_of_documents} with current time {current_time}')
    i+=1
    if 'test' in doc:
        # print(doc['test'])
        if doc['test'] not in tests:
            count_tests+=1
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
print('after iterating results')

print('here are multi tests')
print(multi_tests)

collection = db["testCollections"]


temp = collection.find( {"$and":[{"_id": {"$in":multi_tests} }]}  )
print('here are the test collections from db')

print('tests before')
print(len(tests))
print('calculating count for multi test')
number_of_documents = collection.count_documents({"$and":[{"_id": {"$in":multi_tests} }]})
print(f'we got {number_of_documents} multi tests')

for doc in temp:
    single_tests_from_multi_test = list(map(lambda x: x['testId'], doc['testsForExecutions']))
    tests = list(set(tests) | set(single_tests_from_multi_test))
print('tests after')
print(len(tests))
    # print(doc)
i = 1





collection = db["tests"]
temp = collection.find( {"$and":[{"_id": {"$in":tests} } ,   {"configuration.scriptType" : { "$in": ["jmeter", "taurus"]  }}     ]}  )

print('calculating count for test AFTER excluding non jmeter')
number_of_documents = collection.count_documents({"$and":[{"_id": {"$in":tests} } ,   {"configuration.scriptType" : { "$in": ["jmeter", "taurus"]  }}     ]})

final_test_ids = []
for doc in temp:
    final_test_ids.append(doc['_id'])






for test in tests:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    # print(f'in MULTITEST iteration {i} out of {number_of_documents} with time {current_time}')
    i+=1
    f.write(f'{test}\n')
# print('no tests in these masters')
# print(masters_with_no_test)
#
# print('count of tests')
# print(count_tests)
#
# print('count of no tests')
# print(count_master_no_test)
f.close()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("after time =", current_time)
print('done')





