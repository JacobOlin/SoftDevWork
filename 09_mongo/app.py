from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb://127.0.0.1:27017")
db=client.admin
serverStatusResult=db.command("serverStatus")
