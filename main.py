from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Модель логин + пароль для входа
class User(BaseModel):
    username: str
    password: str

fake_db = {
    "username": "admin",
    "password": "123"
}

app.post("/login")
def login(user:User):
    if user.username in fake_db and fake_db[user.username] == user.password:
        return {"status ok"}
    return {"Status": "Invalid credentials"}