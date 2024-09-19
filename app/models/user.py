from sqlalchemy import Column, String
from api.db.base import Base


class UserModel(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


