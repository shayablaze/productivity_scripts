import requests
import shutil
import os
from os import path
if path.exists("config"):
    shutil.rmtree('config')
os.mkdir('config')


keys_info = {}
with open("jenkins_cookie") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        if var.endswith("\n") or var.endswith("\r"):
            var = var[:-1]
        keys_info[name] = var


cookies = {
    keys_info['key']: keys_info['value']
}

params = (
    ('pretty', 'true'),
)

response = requests.get('http://new-jenkins.blazemeter.com:8080/job/API-TEST-BZA/api/json',  params=params, cookies=cookies, verify=False)

# json_o = response.json()

loaded_json = response.json()
builds = loaded_json['builds']
i =0
for x in builds:
    build_number = x['number']
    print "{0}) build {1}".format(i, build_number)
    response = requests.get('http://new-jenkins.blazemeter.com:8080/job/API-TEST-BZA/{0}/allure/data/suites.csv'.format(build_number), cookies=cookies, verify=False)
    excel = response.content
    if excel.startswith('<html>'):
        print 'build {} not ready'.format(build_number)
    else:
        f = open("config/{}.csv".format(build_number), "w+")
        f.write(excel)
        print 'build {} downloaded successfully'.format(build_number)
        i += 1
    if (i >= 10):
        break



