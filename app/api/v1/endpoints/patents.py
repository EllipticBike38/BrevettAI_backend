from fastapi import APIRouter, Depends
from typing import Optional
from crud.crud_patent import create_patent
from sqlalchemy.orm import Session
from db.session import get_db


router = APIRouter()


#salva un brevetto tuo (l'utente manda il titolo [e corpo] provvisorio)
@router.post("/save_patent/")
async def save_patent(
        name: str,
        body: Optional[str],
        db: Session = Depends(get_db)
) -> None:
    create_patent(1, name, "pending", body, db)

