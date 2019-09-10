import pandas as pd


def objectify_csv(file_name):
    ret = {}
    df = pd.read_csv(file_name, engine='python', encoding='utf-8', error_bad_lines=False)
    for index, row in df.iterrows():
        status = row['Status']
        name = trim_name(row['Name'])
        ret[name] = status

    return ret

# This is because sometimes in the allure report we can get a @3 or @2 for whatever unknown reason.
# All we have to do is get rid of it.


def trim_name(name):
    for x in range(9):
        name = name.replace('API-TEST-BZA@{}'.format(x), 'API-TEST-BZA')
    return name


def initialize_arr_for_counting(arr, key, file_name):
    if arr.get(key):
        arr[key]['count'] = arr[key]['count'] + 1
        arr[key]['file_names'].append(file_name)
    else:
        arr[key] = {'count' : 1, 'file_names':[file_name]}


def less_than(x, y):
    return x < y


def make_comparator():
    def compare(x, y):
        x = x['ratio'].split('/')[0]
        y = y['ratio'].split('/')[0]
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare


def sort_flaky(subjects):
    sorted_dict = sorted(subjects, cmp=make_comparator(), reverse=False)
    return sorted_dict