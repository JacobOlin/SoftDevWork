import pymongo
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db=client.restaurant
restaurant = db.restaurant

file = open("primer-dataset.json", 'r')
data = file.readlines()
file.close()
#print(data)

restaurant.inster_many(documents)

print (restaurant.find({"address.building" : "764"}))
