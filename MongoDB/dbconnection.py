from pymongo import MongoClient
from random import randint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
connection = MongoClient(port=27017)

#mongodb connection
mydb=connection.personaldb
expendituredb=mydb.expenditure


















# print('finished creating 100 business reviews')
# fivestar = db.reviews.find_one({'rating': 5})
# print(fivestar['_id'])

