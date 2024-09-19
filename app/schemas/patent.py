from pydantic import BaseModel
from typing import Optional, List
import uuid


class Patent(BaseModel):
    uuid: uuid.UUID
    name: str
    status: str
    description: Optional[str]


class PatentUpdate(BaseModel):
    name: Optional[str]
    status: Optional[str]
    description: Optional[str]


class PatentList(BaseModel):
    patent_list: List[Patent]