import pandas as pd
def objectify_csv(file_name, remove_skip=True):
    ret = {}
    df = pd.read_csv(file_name)
    for index, row in df.iterrows():
        status = row['Status']
        if status is 'skipped' and remove_skip:
            continue
        name = row['Name']
        ret[name] = status

    return ret