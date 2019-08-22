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
    splitted = name.split('.API-TEST-BZA')
    if len(splitted) != 2:
        print('len of name is not 2: {}'.format(name))
        raise Exception()
    second_half = splitted[1]
    part_under_test = second_half[:1]

    if part_under_test == '@':
        new_second_half = second_half[2:]
        new_name = splitted[0] + '.API-TEST-BZA' + new_second_half
        return new_name
    return name


def initialize_arr_for_counting(arr, key):
    if arr.get(key):
        arr[key] = arr[key] + 1
    else:
        arr[key] = 1

