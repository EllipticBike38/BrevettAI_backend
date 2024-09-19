from fastapi import APIRouter
from typing import Optional
from crud.crud_patent import create_patent
from sqlalchemy.orm import Session
from db.session import SessionLocal

'''
salva un brevetto non tuo (l'utente manda l'id del brevetto preesistente)
recupera tutti i brevetti salati (titoli)
recupera il tuo singolo brevetto
recupera il brevetto di un'altro (tramite query su google patents)
elimina brevetto salvato
'''


router = APIRouter()


#salva un brevetto tuo (l'utente manda il titolo [e corpo] provvisorio)
@router.post("/save_patent/")
async def save_patent(
        name: str,
        body: Optional[str],
        db: Session = SessionLocal()
) -> None:
    patent = create_patent(1, name, "pending", body, db)
    print(patent)


#update del brevetto tuo (l'utente aggiunge/modifica corpo e titolo del brevetto)
# @router.post("/update_patent/")
# async def update_patent(
#         old_name: str,
#         new_name: Optional[str],
#         body: Optional[str]
# ) -> None:
#     for patent in patents:
        