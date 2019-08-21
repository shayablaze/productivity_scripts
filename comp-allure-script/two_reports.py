import pandas as pd
import json
from utils import objectify_csv


def diff_which_tests_ran(file_1, file2):

    object_1 = objectify_csv(file_1, True)
    object_2 = objectify_csv(file2, True)

    only_in_1 = []
    for key, value in object_1.items():
        if key not in object_2.keys():
            only_in_1.append(key)

    only_in_2 = []
    for key, value in object_2.items():
        if key not in object_1.keys():
            only_in_2.append(key)
    pd.read_json(json.dumps(only_in_1)).to_csv('results/only_in_before.csv')
    pd.read_json(json.dumps(only_in_2)).to_csv('results/only_in_after.csv')


file_name_before = 'config/ci.csv'
file_name_after = 'config/new.csv'

before_object = objectify_csv(file_name_before)
after_object = objectify_csv(file_name_after)

diff_which_tests_ran(file_name_before, file_name_after)

diffs_good = []
diffs_bad = []
for key_after, value_after in after_object.items():
    if key_after in before_object.keys():
        before_value = before_object[key_after]
        if before_value != value_after:
            if value_after == 'passed':
                diffs_good.append({
                    'short_name': key_after.split('.')[len(key_after.split('.')) -1],
                    'before_value': before_value,
                    'after_value': value_after,
                    'full_name': key_after,
                })
            else:
                if before_value == 'passed':
                    diffs_bad.append({
                        'short_name': key_after.split('.')[len(key_after.split('.')) -1],
                        'before_value': before_value,
                        'after_value': value_after,
                        'full_name': key_after,
                    })

fin = {
    'good' : diffs_good
}

pd.read_json(json.dumps(diffs_bad)).to_csv('results/regression.csv')

pd.read_json(json.dumps(diffs_good)).to_csv('results/improvement.csv')

print('finished')

