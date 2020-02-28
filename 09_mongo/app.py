import pymongo
from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient('localhost',27017)
db=client.buildings
restaurant = db.restaurant

file = open("primer-dataset.json", 'r')
data = file.readlines()
data = list(map(lambda doc: loads(doc.strip()), data))
file.close()
#print(data)

restaurant.insert_many(data)

#print (restaurant.find({"address.building" : "425"}))

def borough(name):
    return restaurant for restaurant in restaurants.find({"borough": f"{borough}"})

print (borough("bronx"))
