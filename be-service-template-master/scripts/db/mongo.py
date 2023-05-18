
    
from pymongo import MongoClient , ASCENDING
from pydantic import BaseModel
import re
from scripts.constants.app_config import DBConf
from scripts.utility.mongo_utility import MongoServer

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
 
def validate_email(email):
    return bool((re.fullmatch(regex, email)))


mongoclient = MongoServer(DBConf.DB_URI)

student_details = {}
class Student(BaseModel):
    id: int
    name: str
    email: str
    course: str
    age: int




class Reqbody(BaseModel):
   
    email: str


def aggregated_student_data():
    collected_student_data = mongoclient.aggregate_query([{
      "$sort": {
         "id": ASCENDING
      },
   }],DBConf.DB_DATABASE,DBConf.DB_COLLECTION);

    print("collected_student_data",collected_student_data)
    result = []
    for student_data in collected_student_data:
        print(student_data)
        del student_data["_id"]
        result.append(student_data)
    print("result",result)
    return result
    
def add_student(student: Student):
    idStudentExist = mongoclient.find_one({"id": student.id} , DBConf.DB_DATABASE,DBConf.DB_COLLECTION) 

    if idStudentExist :
        return "student already present duplicate ID"

    if validate_email(student.email) == False:
        return "Invalid Email"
    
    mongoclient.insert_one(student.dict(),DBConf.DB_DATABASE,DBConf.DB_COLLECTION)
    
    return "Student added successfully."

def update_student(student_id: int, updated_data: dict):
    print("this is the id of a stu",student_id)
    if list(mongoclient.find_one({"id": student_id},DBConf.DB_DATABASE,DBConf.DB_COLLECTION)) != []:
    
        mongoclient.update_one({"id": student_id},updated_data,DBConf.DB_DATABASE,DBConf.DB_COLLECTION )
        return "Student updated successfully."
    else:
        return "No student found with the provided ID."

def delete_student(student_id: int):
    if list(mongoclient.find_one({"id": student_id},DBConf.DB_DATABASE,DBConf.DB_COLLECTION)) != []:
    
        mongoclient.delete_one({"id": student_id},DBConf.DB_DATABASE,DBConf.DB_COLLECTION )
        return "Student deleted successfully."
    else:
        return "No student found with the provided ID."

def view_students():
    print("here is")
    students = mongoclient.find_many({},DBConf.DB_DATABASE,DBConf.DB_COLLECTION)
    print("This is a student",students)
    students_list = []
    for item in students:
        del item["_id"]
        students_list.append(item)
    if students_list:
        return students_list
    else:
        print("No students found in the database.")


   
