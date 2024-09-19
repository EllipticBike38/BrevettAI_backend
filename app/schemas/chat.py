from pydantic import BaseModel


class Message(BaseModel):
    id: int
    text: str
    order: int


class Chat(BaseModel):
    id: int
    name: str
    messages: list[Message]
