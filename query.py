from pymongo import MongoClient
from bson.json_util import dumps

myclient = MongoClient("localhost")
mydb = myclient.test
mycol = mydb["customers"]
print(dumps(mycol.find()))
