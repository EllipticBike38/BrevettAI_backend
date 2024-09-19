from pydantic import BaseModel


class Patent(BaseModel):
    uuid: str
    name: str
    status: str
    description: str

class PatentUpdate():
    name: str
    status: str
    description: str