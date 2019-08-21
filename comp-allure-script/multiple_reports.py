import pandas as pd
import json
from utils import objectify_csv
import os
# os.remove('config/.DS_Store')
all_files = os.listdir('config')

# print(all_files)

result = {}

for file_name in all_files:
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
    result_nice.append({ 'number_of_failures': value, 'test name': key,})

pd.read_json(json.dumps(result_nice)).to_csv('results/report_mulitple.csv')
print('finished')
# print(result)