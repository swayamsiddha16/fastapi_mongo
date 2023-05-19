from scripts.core.handlers.student_handler import Studenthandler
from fastapi import APIRouter
from scripts.db.mongo import Student,Reqbody
from scripts.constants.app_constants import APIs
from pydantic import BaseModel

Student_rout= APIRouter()

@Student_rout.post(APIs.AGGREGATE_API)
def aggregate_student(body:Reqbody):
    print("thisis the",body)
    studen_obj = Studenthandler()
    return studen_obj.aggregated_data(body.email)
 


@Student_rout.post(APIs.CREATE_API)
def adding_student(student: Student):
    print(student)
    studen_obj = Studenthandler()
    return studen_obj.create_student(student)

@Student_rout.get(APIs.VIEW_API)
def getting_student():
    studen_obj = Studenthandler()
    return studen_obj.get_student()

@Student_rout.put(APIs.UPDATE_API)
def updating_student(student: Student , id : int):
    studen_obj = Studenthandler()
    return studen_obj.student_update(id, student.dict())

@Student_rout.delete(APIs.DELETE_API)
def deleting_student( student_id : int):
    studen_obj = Studenthandler()
    return studen_obj.del_student(student_id)

@Student_rout.get('/student/view/{id}')
def getting_student_byid(id : int):
    print(id)
    studen_obj = Studenthandler()
    return studen_obj.get_student_byId(id)

@Student_rout.get('/student/bykey/{key}/{val}')
def getting_student_bykey(key:str,val:str):
    print(key,val)
    studen_obj = Studenthandler()
    if key in ["id","age"]:
        return studen_obj.get_student_bykey(key,int(val))
        
    return studen_obj.get_student_bykey(key,val)

