from sqlalchemy import Column, Integer, String
from api.db.base import Base


class UserModel(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


class PatentModel(Base):
    __tablename__ = "patents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)  # "completed" or "pending"
    description = Column(String)