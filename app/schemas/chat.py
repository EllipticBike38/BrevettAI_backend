from pydantic import BaseModel

class Chat(BaseModel):
    id: int
    name: str
    path: str

    
class Message(BaseModel):
    text: str

