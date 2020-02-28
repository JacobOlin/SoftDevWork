import pymongo
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db=client.restaurant

file = open("primer-dataset.json", 'r')
data = file.readlines()
print(data)
