from pymongo import MongoClient
import json

client = MongoClient()
db=client.buildings
restaurant = db.restaurant

rawdata = open('primer-dataset.json').read()
data = json.loads(rawdata)
restaurant.insert_many(data)
#print(data)


#print (restaurant.find({"address.building" : "425"}))

def borough(name):
    return list(restaurant.find({"borough": name}))

def zipcode(number):
    return list(restaurant.find({"zipcode": name}))

def zipcode_grade(zipcode, grade):
    return list(restaurant.find({"zipcode": zipcode, "grades.grade": grade}))

def zipcode_score(zipcode, score):
    return list(restaurant.find({"zipcode": zipcode, "grades.score": {$lt: score}}))

print (borough("bronx"))
