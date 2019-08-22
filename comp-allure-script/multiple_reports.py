import pandas as pd
import json
from utils import objectify_csv
from utils import initialize_arr_for_counting
import os
# os.remove('config/.DS_Store')
the_files = os.listdir('config')
number_of_runs = len(the_files)
print(number_of_runs)


def find_flakiness(tests_list, type):
    nicely_formatted_arr = []
    consistent = []
    flaky = []
    for key,value in tests_list.items():
        nicely_formatted_arr.append({'number_of_appearances': value, 'test name': key})
    for elem in nicely_formatted_arr:
        if elem.get('number_of_appearances') == number_of_runs:
            consistent.append(elem.get('test name'))
        else:
            flaky.append({'test name': elem.get('test name'), 'ratio':'{0}/{1}'.format(elem.get('number_of_appearances'), number_of_runs) })
    pd.read_json(json.dumps(flaky)).to_csv('results/report_flaky_{}.csv'.format(type))
    pd.read_json(json.dumps(consistent)).to_csv('results/report_consistent_{}.csv'.format(type))


tests_that_failed = {}
tests_that_ran = {}
tests_that_skipped = {}

for file_name in the_files:
    print(file_name)
    current_object = objectify_csv('config/' + file_name)
    for key,value in current_object.items():
        if value not in ['passed', 'skipped']:
            initialize_arr_for_counting(tests_that_failed, key)
        if value != 'skipped':
            initialize_arr_for_counting(tests_that_ran, key)
        if value == 'skipped':
            initialize_arr_for_counting(tests_that_skipped, key)

find_flakiness(tests_that_failed, 'failures')
find_flakiness(tests_that_ran, 'runs')

print('finished')

