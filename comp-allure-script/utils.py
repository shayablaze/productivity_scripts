import pandas as pd


def objectify_csv(file_name):
    ret = {}
    df = pd.read_csv(file_name)
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


def initialize_arr_for_counting(arr, key):
    if arr.get(key):
        arr[key] = arr[key] + 1
    else:
        arr[key] = 1

