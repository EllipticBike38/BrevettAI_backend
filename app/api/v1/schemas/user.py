from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Message(BaseModel):
    text: str

class Chat(BaseModel):
    name: str

class Patent(BaseModel):
    title: str
    status: str
