# for run api you need 4 infor 
# Route 
# method = get / post / 
# ip address 
# posrt # 8080

# 1----------------------
from fastapi import FastAPI
import uvicorn 

# 2----------------------
app = FastAPI()


# 3  app called the function form outside ------------------------
@app.get("/gettodos")

# 4 def a function gettodo()--------------
def gettodos():
    print("get todos called ")
    return "gettodos called" 
# called manually-------------------
# gettodos()

# # POST API-------------------------
@app.post("/postTodo")

def postTodo():
    print("print postTodo ")
    return "Return postTodo"

# 5  function by diff /Route  ------------------------
@app.get("/getSingleTodo")
def getSingleTodo():
    # print("getSingleTodo is called ")
    return "getSingleTodo has been returned"

# #   Test function   ------------------------
# @app.get("/")
# def testfunction():
#     print("print test function ")
#     return "Return testfunction"

#   update function   ------------------------
@app.put("/updateTodo")
def updateTodo():
    return "Return updateTodo"



# 6 start a function uvcorn ----------------------
# 
def start():
    # todos is folder and main.py id file ,, reload=True Refresh auto
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8011, reload=True)
    
    

# # 7  Test function True / False    ------------------------
# @app.get("/testApi")
# def testApi():
#     return True

# # 8  Test function True / False    ------------------------
# @app.get("/testApi")
# def testApi():
#     return [1,2,3]

# # 9  Dictionary send    ------------------------
# @app.get("/testApi")
# def testApi():
#     return ["dictionary","has","been","return"]

# # 10  JSON or Rest api Respone send by put { : }  in dictionary     ------------------------
# @app.get("/testApi")
# def testApi():
#     return {"dictionary":"return"}

# 11  Return by id by path variable/dynamic path to get data from fromtend     ------------------------
# http://127.0.0.1:8011/returnByIdFun/id     id = may be 12,13.....................................
# http://127.0.0.1:8011/returnbyidfun/13    ..................................

@app.get("/returnByIdFun/{id}")
def returnByIdFun(id):
    print("print to Get by id  ", id)
    return id

# 12  Return by id by dynamic path to get data from 2 items userName + rollNo     ------------------------
# http://127.0.0.1:8011/returnUserNameRoll/userNam/rollNo     id = may be 12,13....................................
# http://127.0.0.1:8011/returnUserNameRoll/hassan/12    ..................................

@app.get("/returnUserNameRoll/{userName}/{rollNO}")
def returnUserNameRoll(userName:str , rollNO:str):
    print("print to Get by id  ", userName , rollNO)
    return userName + rollNO


# 13  Query param to send data without path     ------------------------
# http://127.0.0.1:8011/qParam/userNam/rollNo     id = may be 12,13....................................
# http://127.0.0.1:8011/qParam/    ..................................

@app.get("/qParam/{userName}/{rollNo}")
def qParam(userName:str , rollNo:str):
    print("print to Get by qParam  ", userName , rollNo)
    return "Return by qParam"


# 14  Query param to send data without path     ------------------------
# http://127.0.0.1:8011/students/    ..................................

# app = FastAPI()

students = [
    {
    "userName": "Hassan",
    "rollNo":   1111
    },
    {
    "userName": "Hassan2",
    "rollNo":   2222
    }
    
        ]

@app.get("/students")
def getStudents():
    return students

# Add student in qParam ...................................
# http://127.0.0.1:8011/addStudent/    ..................................check on postman 

@app.get("/addStudent")
def addStudent(userName:str , rollNo:str):
    global students
    students.append({"userName":userName, "rollNo":rollNo})
    return students

# Remove student in qParam ...................................
# http://127.0.0.1:8011/removeStudent/    ..................................check on postman 
#  http://127.0.0.1:8011/removeStudent/?userName=Hassan2&rollNo=2222    ..................................check on postman 

@app.delete("/removeStudent")
def removeStudent(userName:str , rollNo:str):
    global students
    # students.remove({"userName":userName, "rollNo":rollNo})
    students = (student["userName"] == userName and student["rollNo"] == rollNo)
    return students

# Remove student in qParam ...................................
# http://127.0.0.1:8011/updateStudent/    ..................................check on postman 
#  http://127.0.0.1:8011/updateStudent/?userName=Hassan3&rollNo=3332    ..................................check on postman 

@app.put("/updateStudent")
def updateStudent(userName:str , rollNo:str):
    global students
    students.update({"userName":userName, "rollNo":rollNo})
    return students





