from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = {}

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    if user.username in users:
        raise HTTPException(400, "User already exists")
    users[user.username] = user.password
    return {"message": "Registered"}

@app.post("/login")
def login(user: User):
    if users.get(user.username) != user.password:
        raise HTTPException(401, "Invalid credentials")
    return {"message": "Login successful"}

@app.get("/me/{username}")
def get_user(username: str):
    if username not in users:
        raise HTTPException(404, "User not found")
    return {"username": username}
