import uuid
from sqlalchemy import Column, String
from db.base import Base
from sqlalchemy.dialects.postgresql import UUID

class PatentModel(Base):
    __tablename__ = "patents"

    uuid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    status = Column(String)  # "completed" or "pending"
    description = Column(String, nullable=True)
