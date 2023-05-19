import json
import traceback
from pymongo import MongoClient



"""
MONGO UTILITY : This utility will have all the CRUD operation
used for mongo db
"""
from pymongo import MongoClient

from scripts.constants.app_config import DBConf


class MongoServer:
    """
    This is MONGO SERVER class which will contain all the mongo methods
    """
    def __init__(self, mongo_URI):
        try:
            self.__mongo_OBJ__ = MongoClient(
                 mongo_URI    
            )
        except Exception as e:
            raise Exception(str(e))
        print("this is constructor",self.__mongo_OBJ__["interns_b2_23"]["swayamsiddha_student"].find())


   
        
    
    def find_one(self, condition, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            return database_connection[collection_name].find_one(condition)
        
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
       
    
    def find_many(self, condition, database_name, collection_name):
        print("this the data",database_name,collection_name)
        print(self.__mongo_OBJ__)
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            return database_connection[collection_name].find(condition)
            
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
       
    
   
    def insert_one(self, json_data, database_name, collection_name):
        try:
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_one(json_data)
            return mongo_response.inserted_id
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
    
    def insert_many(self, json_data, database_name, collection_name):
        try:
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_many(json_data)
            json_mongo_response_object = json.loads(json.dumps(mongo_response))
            return json_mongo_response_object
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
    
    def update_one(self, condition , json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_one(condition,{"$set": json_data})
            return "success"
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
        
    def update_many(self, condition, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_many(condition, {"$set": json_data})
            return "success"
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
        
    def delete_one(self, condition, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].delete_one(condition)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
        
    def delete_many(self, condition, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].delete_many(condition)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))
        
    
    def aggregate_query(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].aggregate(json_data)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))


    
   
    

    
    
    
    
 
    