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

#   function   ------------------------
# @app.get("/")
# def testfunction():
#     print("print test function ")
#     return "Return test function"

#   update function   ------------------------
@app.put("/updateTodo")
def updateTodo():
    return "Return updateTodo"



# 6 start a function uvcorn ----------------------
# 
def start():
    # todos is folder and main.py id file ,, reload=True Refresh auto
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8011, reload=True)
    
    

