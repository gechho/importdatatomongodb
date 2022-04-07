# build virtual environment for python
# python -m venv pyvenv
# activate python venv
# c:/Practice/venv/Scripts/Activate.bat
# install pandas in virtual environment in windows
import pandas as pd
from pymongo import MongoClient
import json
import pymongo 
import credential
# convert csv to json format
# csvfile='C:\Practice\csv2mongodb\titanic.csv'
# You need use a raw string for the path variable, or escape the backslash:
df = pd.read_csv(r'C:\Practice\csv2mongodb\titanic.csv')
# df.to_json('yourjson.json',orient = "records")                               # saving to json file
# # loading the json file
# jdf = open('yourjson.json').read()
# file_data = json.loads(jdf)
print(df)
file_data= json.loads(df.to_json(orient = "records"))


# print(file_data)
# convert json data to mongodb database
connection_string = "mongodb+srv://" + credential.username + ":" + credential.password +  "@sandbox.1dwlg.mongodb.net/python?retryWrites=true&w=majority"

print(connection_string)
#myclient = MongoClient(connection_string)
# db=myclient["importeddata"]
# Collection = db["titanic"]
# Collection.insert_one(file_data)



# import json file into mongodb
# Making Connection
myclient = MongoClient('localhost', 27017) 
db=myclient["sandbox"]
Collection = db["titanic2"]
print(myclient.list_database_names())
#bsonx = BSON.encode(jsonx)

Collection.insert_many(file_data)
#  test