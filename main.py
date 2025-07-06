from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel): #модель пользователя
    name : str
    password : str

class Token(BaseModel): #модель токена
    access_token: str

#создаем пока фейковую bd потом заменить на нормальную
fake_bd = {
    "admin" : {
        "Username" : "admin",
        "Password" : "123"
    }
}

@app.get("/")
async def root():
    return ("Hello")

