from pydantic import BaseModel


class Message(BaseModel):
    id: str
    text: str
    order: int


class Chat(BaseModel):
    id: str
    name: str
    messages: list[Message]
