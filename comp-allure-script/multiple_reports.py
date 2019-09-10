import pandas as pd
import json
from utils import objectify_csv
from utils import sort_flaky
from utils import initialize_arr_for_counting
import os
from os import path
import shutil
import requests

if path.exists("config"):
    shutil.rmtree('config')
os.mkdir('config')

if path.exists("results"):
    shutil.rmtree('results')
os.mkdir('results')

keys_info = {}
with open("jenkins_cookie") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        if var.endswith("\n") or var.endswith("\r"):
            var = var[:-1]
        keys_info[name] = var


cookies = {
    keys_info['key']: keys_info['value']
}

params = (
    ('pretty', 'true'),
)

response = requests.get('http://new-jenkins.blazemeter.com:8080/job/API-TEST-BZA/api/json',  params=params, cookies=cookies, verify=False)

# json_o = response.json()

loaded_json = response.json()
builds = loaded_json['builds']
# i =0
# for x in builds:
#     build_number = x['number']
#     print "{0}) build {1}".format(i, build_number)
#     response = requests.get('http://new-jenkins.blazemeter.com:8080/job/API-TEST-BZA/{0}/allure/data/suites.csv'.format(build_number), cookies=cookies, verify=False)
#     excel = response.content
#     if excel.startswith('<html>') or build_number > 1293 or build_number==1292:
#         print 'build {} not ready'.format(build_number)
#     else:
#         f = open("config/{}.csv".format(build_number), "w+")
#         f.write(excel)
#         print 'build {} downloaded successfully'.format(build_number)
#         i += 1
#     if (i >= 2):
#         break

build_numbers = [1340, 1339, 1338, 1337, 1336, 1335, 1334, 1333, 1332]
for x in build_numbers:
    build_number = x
    print " build {0}) ".format( build_number)
    response = requests.get('http://new-jenkins.blazemeter.com:8080/job/API-TEST-BZA/{0}/allure/data/suites.csv'.format(build_number), cookies=cookies, verify=False)
    excel = response.content
    if excel.startswith('<html>'):
        print 'build {} not ready'.format(build_number)
    else:
        f = open("config/{}.csv".format(build_number), "w+")
        f.write(excel)
        print 'build {} downloaded successfully'.format(build_number)
    #     i += 1
    # if (i >= 10):
    #     break





if path.exists("config/.DS_Store"):
    os.remove('config/.DS_Store')
the_files = os.listdir('config')

for a_file_name in the_files:
    file_extension = a_file_name.split('.')[len(a_file_name.split('.')) -1]
    if file_extension != 'csv':
        print('*******non csv file found {}***********'.format(file_extension) )
        raise Exception('non csv file found')

number_of_runs = len(the_files)


def find_flakiness(tests_list, type):
    nicely_formatted_arr = []
    consistent = []
    flaky = []
    for key,value in tests_list.items():
        nicely_formatted_arr.append({'number_of_appearances': value['count'], 'test name': key, 'file_names': value['file_names']})
    for elem in nicely_formatted_arr:
        if elem.get('number_of_appearances') == number_of_runs:
            consistent.append(elem.get('test name'))
        else:
            flaky.append({'test name': elem.get('test name'), 'ratio':'{0}/{1}'.format(elem.get('number_of_appearances'), number_of_runs), 'file_names' : elem.get('file_names')})


    flaky = sort_flaky(flaky)

    pd.read_json(json.dumps(flaky)).to_csv('results/report_flaky_{}.csv'.format(type))
    pd.read_json(json.dumps(consistent)).to_csv('results/report_consistent_{}.csv'.format(type))


tests_that_failed = {}
tests_that_existed = {}
tests_that_skipped = {}

for file_name in the_files:
    print 'before objectifying file {0}'.format(file_name)
    current_object = objectify_csv('config/' + file_name)
    for key,value in current_object.items():
        if value not in ['passed', 'skipped']:
            initialize_arr_for_counting(tests_that_failed, key, file_name)
        if value == 'skipped':
            initialize_arr_for_counting(tests_that_skipped, key, file_name)
        initialize_arr_for_counting(tests_that_existed, key, file_name)

find_flakiness(tests_that_failed, 'failures')
find_flakiness(tests_that_existed, 'exist')
find_flakiness(tests_that_skipped, 'skips')

print('finished')

