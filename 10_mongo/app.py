#Tyler Huang, Jacob Olin, Hillary Zen
#Team Sticky Sulphur
#SoftDev pd 2
#K10 -- Import/Export Bank
#2020-03-04

from pymongo import MongoClient
from pprint import pprint
import datetime
import json

client = MongoClient("mongodb://admin:thuang@64.225.14.222/")
db = client.stickySulphur
col = db.senators

def findParty(party):
        for senator in col.find({"party": party}):
                print(col["name"])

findParty("Republican")
