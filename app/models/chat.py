import uuid
from sqlalchemy import Column, ForeignKey, String, Integer, Uuid
from sqlalchemy.orm import relationship
from db.base import Base


class ChatModel(Base):
    __tablename__ = "chats"

    id_ = Column(String, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True)
    messages = relationship(
        "Message", back_populates="chat", cascade="all, delete-orphan"
    )


class Message(Base):
    __tablename__ = "messages"

    id_ = Column(String, primary_key=True, index=True, default=uuid.uuid4)
    text = Column(String)
    order = Column(Integer)

    chat_uuid = Column(String, ForeignKey("chats.uuid"))
    chat = relationship("ChatModel", back_populates="messages")
