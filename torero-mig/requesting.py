import requests
from requests.auth import HTTPBasicAuth

is_prod = False


key_id_dev = '41e52a6c6718dcdab317780c'
key_secret_dev = 'd059a47cb764c169320fd9ae62976857d1b35d3b828620d108093e1d6846eb568b784353'
auth_dev = HTTPBasicAuth(key_id_dev, key_secret_dev)
url_dev = 'https://bza-5352-shayaa-gcp.blazemeter.net'


key_id_prod = '53c42d6dd11745ca8c6acc9c'
key_secret_prod = 'acab89bd26c3c88c88843a141ddd4613752712511e3fedbbfc0163fb814a374f784c5fea'
auth_prod = HTTPBasicAuth(key_id_prod, key_secret_prod)
url_prod = 'https://prod-rc.blazemeter.com'

params = {
    'shouldLoop': 'false',
    'numberOfTestsPerLoop': 1,
    'delayInSeconds': 10,
}

json_data = {
    'accountIds': [
        # 6
    ],
}


if is_prod:
    response = requests.post(f'{url_prod}/api/v4/admin/migrate-torero-list', params=params, auth=auth_prod, json=json_data)
else:
    response = requests.post(f'{url_dev}/api/v4/admin/migrate-torero-list', params=params, auth=auth_dev, json=json_data)

print (response.json()['result'])