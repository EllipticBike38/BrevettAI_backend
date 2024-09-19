from typing import List, Optional
from pydantic import BaseModel


class Patent(BaseModel):
    uuid: str
    name: str
    status: str
    description: Optional[str]


class PatentUpdate(BaseModel):
    name: Optional[str]
    status: Optional[str]
    description: Optional[str]


class PatentList(BaseModel):
    patent_list: List[Patent]