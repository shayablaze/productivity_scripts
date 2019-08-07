import pandas as pd
import json


def objectify_csv(file_name):
    ret = {}
    df = pd.read_csv(file_name)
    for index, row in df.iterrows():
        status = row['Status']
        if status != 'skipped':
            name = row['Name']
            ret[name] = status
    return ret


file_name_before = 'config/before.csv'
file_name_after = 'config/after.csv'

before_object = objectify_csv(file_name_before)
after_object = objectify_csv(file_name_after)

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

