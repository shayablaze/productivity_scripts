import requests
print('inside me requesting')
response = requests.get('http://localhost:5555/do-this')
print(f"Called mememememememmememememmemememe /do-this: {response.status_code}")