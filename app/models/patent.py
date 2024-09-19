from sqlalchemy import Column, Integer, String
from api.db.base import Base


class PatentModel(Base):
    __tablename__ = "patents"

    uuid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)  # "completed" or "pending"
    description = Column(String)