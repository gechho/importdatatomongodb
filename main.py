# read csv file in python
import pandas as pd
import json

from pymongo import MongoClient


#excelfile = open('C:/Practice/titanic.xlsx','r')

excelfile ='C:/Practice/titanic2.xlsx'

df = pd.read_excel(excelfile)
#print(df)



# transform python dataframe to json format

jsonx = json.loads(df.to_json(orient = "records"))

# import json file into mongodb
# Making Connection
myclient = MongoClient('localhost', 27017) 
db=myclient["sandbox"]
Collection = db["titanic"]
print(myclient.list_database_names())
#bsonx = BSON.encode(jsonx)


Collection.insert_many(jsonx)

#print(myclient.list_database_names())