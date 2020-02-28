from pymongo import MongoClient
import json

client = MongoClient()
db=client.buildings
restaurant = db.restaurant
restaurant.delete_many({})


with open("primer-dataset.json", 'r') as file:
    data = json.load(file)
    for item in data:
        restaurant.insert_one(loads(json.dumps(item)))

#print(data)


#print (restaurant.find({"address.building" : "425"}))

def borough(name):
    return list(restaurant.find({"borough": name}))

def zipcode(number):
    return list(restaurant.find({"address.zipcode": name}))

def zipcode_grade(zipcode, grade):
    return list(restaurant.find({"address.zipcode": zipcode, "grades.0.grade": grade}))

def zipcode_score(zipcode, score):
    return list(restaurant.find({"address.zipcode": zipcode, "grades.0.score": {"$lt": score}}))

print (borough("bronx"))
