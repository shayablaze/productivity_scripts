import json,sys,requests
import time
from get_tokens import get_tokens
from requests.auth import HTTPBasicAuth
api_key = get_tokens('api_key')
secret = get_tokens('secret')

auth = HTTPBasicAuth(api_key, secret)
url = 'https://bza-126-ajzye01-shayablaze.env.blazemeter.net/api/v4/masters?limit=10&workspaceId=2'
response = requests.get(url, auth=auth)
result = response.json()['result']
arr = []
auth = HTTPBasicAuth(api_key, secret)
for master in result:
    master_id = str(master['id'])
    url = 'https://bza-126-ajzye01-shayablaze.env.blazemeter.net/api/v4/masters/' + master_id + '/terminate'

    response = requests.post(url, auth=auth)
    arr.append(master_id)
print arr
bad_arr = list(arr)

while len(bad_arr) is not 0:
    for master_id in bad_arr:
        url ='https://bza-126-ajzye01-shayablaze.env.blazemeter.net/api/v4/masters/'+ master_id + '/status'
        response = requests.get(url, auth=auth)
        is_ended = response.json()['result']['status'] == 'ENDED'

        if is_ended:
            print 'ended good!!!!'
            bad_arr.remove(master_id)
        time.sleep(1)

for master_id in arr:
    url = 'https://bza-126-ajzye01-shayablaze.env.blazemeter.net/api/v4/masters/' + master_id
    response = requests.delete(url, auth=auth)



print 'all done!'
