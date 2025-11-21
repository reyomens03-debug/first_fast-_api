from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
#Create fastAPI app
app =FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
#Use BaseModel form pydantic
class Student(BaseModel):
    id : int
    name : str 
    grade : int
#Create list for DATA
students =[
    Student(id=1,name="ali asfor",grade=11),
    Student(id=2,name="ahmed ahmed",grade=10)
]
#read all objekt
@app.get("/students/")
def read_students():
    return students
#create new objekt
@app.post("/students/")
def create_student(New_Student:Student):
    students.append(New_Student)
    return New_Student
#Update objekt
@app.put("/students/{student_id}")
def update_student(student_id:int, update_student: Student):
    for index,student in enumerate(students):
        if student.id == student_id:
            students[index] =update_student
            return update_student
    return {"error" : "Student not found"}
#Delete objekt
@app.delete("/students/{student_id}")
def delete_student(student_id:int, delete_student: Student):
    for index,student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message" : "Student delete"}
    return {"error" : "Student not found"}




