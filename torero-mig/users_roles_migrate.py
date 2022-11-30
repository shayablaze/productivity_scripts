from datetime import datetime
import pandas as pd
import sys
import openpyxl
from jproperties import Properties
from pymongo import MongoClient
from bson import ObjectId
p = Properties()
import os
with open("props", "rb") as f:
    p.load(f, "utf-8")
user = p.properties['user']
password = p.properties['password']
database_address = 'prod-main.ewwd2.mongodb.net'
database_name = 'blazemeter'
mongo_string_blaze = f'mongodb+srv://{user}:{password}@{database_address}/{database_name}'

cluster = MongoClient(mongo_string_blaze)

db = cluster['blazemeter']
collection = db['users']

# query = { {'$and': [ { '_id': {'$in' : [1225166]}},  {'roles':{'$type' : 'object'}}]}   }

query = { '$and': [ { '_id': {'$in' : [1225166] } }]   }
query = { '$and': [ { 'roles': {'$type' : 'object'} }]   }

users = collection.find( query )

i = 1

for user in users:

    keys = list(user['roles'].keys())
    non_numerics = list(filter(lambda x : not x.isnumeric(), keys))

    if non_numerics:
        raise Exception('got illegal one')
    first_name =  user['firstName']
    print(f'{i}) {first_name}')
    print(user['roles'])
    print(list(user['roles'].values()))

    i +=1