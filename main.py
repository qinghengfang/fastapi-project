from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get('/')  #we access the root path
async def read_root():
    return {"message":"Hello World"}

# {} the var we want to pass to the server
@app.get('/greet/{name}')
async def greet_name(name: Optional[str] = "User",
                     age: int = 0) -> dict:
    return {"message":f"Hello {name}", "age":age}


   