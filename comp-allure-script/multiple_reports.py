import pandas as pd
import json
from utils import objectify_csv
from utils import initialize_arr_for_counting
import os
# os.remove('config/.DS_Store')
the_files = os.listdir('config')
number_of_runs = len(the_files)
print(number_of_runs)

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


tests_that_failed_nicely_formatted = []

for key,value in tests_that_failed.items():
    tests_that_failed_nicely_formatted.append({'number_of_failures': value, 'test name': key})

# pd.read_json(json.dumps(tests_that_failed_nicely_formatted)).to_csv('results/report_mulitple.csv')


consistent_failures = []
flaky = []

for elem in tests_that_failed_nicely_formatted:
    if elem.get('number_of_failures') == number_of_runs:
        consistent_failures.append(elem.get('test name'))
    else:
        flaky.append({'test name': elem.get('test name'), 'ratio':'{0}/{1}'.format(elem.get('number_of_failures'), number_of_runs) })
pd.read_json(json.dumps(flaky)).to_csv('results/report_flaky_failures.csv')
pd.read_json(json.dumps(consistent_failures)).to_csv('results/report_consistent_failures.csv')



########METAL RULES########
tests_that_ran_nicely_formatted = []

for key,value in tests_that_ran.items():
    tests_that_ran_nicely_formatted.append({'number_of_runs': value, 'test name': key})

consistent_runs = []
flaky_runs = []

for elem in tests_that_ran_nicely_formatted:
    if elem.get('number_of_runs') == number_of_runs:
        consistent_runs.append(elem.get('test name'))
    else:
        flaky_runs.append({'test name': elem.get('test name'), 'ratio':'{0}/{1}'.format(elem.get('number_of_runs'), number_of_runs) })
pd.read_json(json.dumps(flaky_runs)).to_csv('results/report_flaky_runs.csv')
pd.read_json(json.dumps(consistent_runs)).to_csv('results/report_consistent_runs.csv')

print('finished')


# print(result)