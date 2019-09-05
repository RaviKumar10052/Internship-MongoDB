from pymongo import MongoClient
import os

client = MongoClient["localhost"]
os.system("mongo")
os.system("show dbs")