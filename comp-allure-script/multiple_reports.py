import pandas as pd
import json
from utils import objectify_csv
import os
# os.remove('config/.DS_Store')
the_files = os.listdir('config')
number_of_runs = len(the_files)
print(number_of_runs)

result = {}

for file_name in the_files:
    print(file_name)
    current_object = objectify_csv('config/' + file_name)
    for key,value in current_object.items():
        if value not in ['passed', 'skipped']:
            if result.get(key):
                result[key] = result[key] + 1
            else:
                result[key] = 1

result_nice = []

for key,value in result.items():
    result_nice.append({ 'number_of_failures': value, 'test name': key})

pd.read_json(json.dumps(result_nice)).to_csv('results/report_mulitple.csv')


consistent = []
flaky = []

for elem in result_nice:
    if elem.get('number_of_failures') == number_of_runs:
        consistent.append(elem.get('test name'))
    else:
        flaky.append({'test name': elem.get('test name'), 'ratio':'{0}/{1}'.format(elem.get('number_of_failures'), number_of_runs) })
pd.read_json(json.dumps(flaky)).to_csv('results/report_flaky.csv')
pd.read_json(json.dumps(consistent)).to_csv('results/report_consistent.csv')

print('finished')


# print(result)