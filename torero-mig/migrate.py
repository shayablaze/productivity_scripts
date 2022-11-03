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

query = {"$and":[{"_id": {"$in":[65116796, 65116801, 65116804, 65117337, 65118005, 65118135]} }]}

temp = collection.find( query )

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
number_of_documents = collection.count_documents(query)
print(f'we got {number_of_documents} masters')

if number_of_documents == 0:
    print('good bye')
    exit()

test_info = {

}
for doc in temp:

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    # print(f'in test iteration {i} out of {number_of_documents} with current time {current_time}')
    i+=1
    if 'test' in doc:
        # print(doc['test'])

        project = doc['project']
        if project not in test_info:
            test_info[project] = { 'tests' : [], 'testCollection':[]  }
        temp_tests = test_info[project]['tests']
        temp_tests = list(set(temp_tests) | set([doc['test']]))
        test_info[project]['tests'] = temp_tests

    elif 'testCollection' in doc:

        project = doc['project']
        if project not in test_info:
            test_info[project] = { 'tests' : [], 'testCollection':[]  }

        temp_tests = test_info[project]['testCollection']
        temp_tests = list(set(temp_tests) | set([doc['testCollection']]))
        test_info[project]['testCollection'] = temp_tests

    else:
        master_id = doc['_id']
        # print(f'no test wtf with master: {master_id}')
        masters_with_no_test = list(set(masters_with_no_test) | set([doc['_id']]))
        count_master_no_test +=1

projects = list(test_info.keys())

collection = db["projects"]


query = {"$and":[{"_id": {"$in":projects} }]}

temp = collection.find( query )

workspaces = []
test_info_by_workspace = {}
for doc in temp:
    workspace_id = doc['workspace']
    workspaces = list(set(workspaces) | set([workspace_id]))
    project_id = doc['_id']
    if workspace_id not in test_info_by_workspace:
        test_info_by_workspace [workspace_id] = { 'tests' : [], 'testCollection':[]  }

    test_info_by_workspace [workspace_id]['tests']+= test_info[project_id]['tests']
    test_info_by_workspace [workspace_id]['testCollection'] += test_info[project_id]['testCollection']

print(test_info)
print(len(list(test_info.keys())))
print(test_info_by_workspace)
print(len(list(test_info_by_workspace.keys())))
print(workspaces)


collection = db["accounts"]


query = {"$and":[{"workspaces": {"$in":workspaces} }]}

temp = collection.find( query )

accounts = []
test_info_by_account = {}
for doc in temp:
    account_id = doc['_id']
    workspaces_from_account = doc['workspaces']
    for workspace_id in workspaces_from_account:
        if workspace_id in test_info_by_workspace:
            if account_id not in test_info_by_account:
                test_info_by_account [account_id] = { 'tests' : [], 'testCollection':[]  }
            test_info_by_account [account_id]['tests']+= test_info_by_workspace[workspace_id]['tests']
            test_info_by_account [account_id]['testCollection'] += test_info_by_workspace[workspace_id]['testCollection']


print(len(list(test_info_by_account.keys())))
print(test_info_by_account)
print(list(test_info_by_account.keys()))
print('done rose')



# print('after iterating results')
#
# print('here are multi tests')
# print(multi_tests)
#
# collection = db["testCollections"]
#
#
# temp = collection.find( {"$and":[{"_id": {"$in":multi_tests} }]}  )
# print('here are the test collections from db')
#
# print('tests before')
# print(len(tests))
# print('calculating count for multi test')
# number_of_documents = collection.count_documents({"$and":[{"_id": {"$in":multi_tests} }]})
# print(f'we got {number_of_documents} multi tests')
#
# for doc in temp:
#     single_tests_from_multi_test = list(map(lambda x: x['testId'], doc['testsForExecutions']))
#     tests = list(set(tests) | set(single_tests_from_multi_test))
# print('tests after')
# print(len(tests))
#     # print(doc)
# i = 1
#
#
#
#
#
# collection = db["tests"]
# temp = collection.find( {"$and":[{"_id": {"$in":tests} } ,   {"configuration.scriptType" : { "$in": ["jmeter", "taurus"]  }}     ]}  )
#
# print('calculating count for test AFTER excluding non jmeter')
# number_of_documents = collection.count_documents({"$and":[{"_id": {"$in":tests} } ,   {"configuration.scriptType" : { "$in": ["jmeter", "taurus"]  }}     ]})
#
# final_test_ids = []
# for doc in temp:
#     final_test_ids.append(doc['_id'])
#
#
#
#
#
#
# for test in tests:
#     now = datetime.now()
#
#     current_time = now.strftime("%H:%M:%S")
#     # print(f'in MULTITEST iteration {i} out of {number_of_documents} with time {current_time}')
#     i+=1
#     f.write(f'{test}\n')
# # print('no tests in these masters')
# # print(masters_with_no_test)
# #
# # print('count of tests')
# # print(count_tests)
# #
# # print('count of no tests')
# # print(count_master_no_test)
# f.close()
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("after time =", current_time)
# print('done')
#
#
#
#
#
