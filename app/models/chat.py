from sqlalchemy import Column, String, Integer
from db.base import Base


class ChatModel(Base):
    __tablename__ = "chats"

    uuid = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    path = Column(String)


