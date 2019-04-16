import os
import requests
from scrapy import Selector
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.db
collection = db.company
for i in range(1,21):
    company = {
        'id':str(i),
        'name':'上海'
    }
result = collection.insert(company)
