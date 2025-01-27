import requests
import sys

file_path = sys.argv[1]
print('inside me requesting')
url = 'http://localhost:5555/do-this'
params = {'file_path': file_path}
response = requests.post(url, params=params)
print(f"Called mememememememmememememmemememe /do-this: {response.status_code}")
print(f"Called with response /do-this: {response.text}")