from fastapi import APIRouter, Depends
from typing import Optional
from ....crud.crud_patent import create_patent, get_patents, remove_patent
from sqlalchemy.orm import Session
from ....db.session import get_db

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
        db: Session = Depends(get_db)
) -> None:
    create_patent(1, name, "pending", body, db)


#update del brevetto tuo (l'utente aggiunge/modifica corpo e titolo del brevetto)
@router.post("/update_patent/")
async def update_patent(
        old_name: str,
        new_name: Optional[str],
        body: Optional[str]
) -> bool:
    if new_name is None and body is None:
                return False
    for patent in get_patents():
        if patent["name"] == old_name:
            if new_name is not None:
                patent["name"] = new_name
            if body is not None:
                patent["description"] = body
            
            return True
    return False

@router.get("/get_patents/")
async def get_patents():
    return get_patents()

@router.get("/get_patent/")
async def get_patent(
        name: str
):
    for patent in get_patents():
        if patent["name"] == name:
            return patent
    return None

@router.post("/delete_patent/")
async def delete_patent(
        name: str
) -> bool:
    for patent in get_patents():
        if patent["name"] == name:
            remove_patent(name)
            return True
    return False
        

        