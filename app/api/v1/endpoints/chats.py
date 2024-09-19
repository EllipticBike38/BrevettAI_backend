from fastapi import APIRouter, Depends, HTTPException

from schemas.chat import Chat, Message as MessageResponse
from crud.crud_chat import create_chat, create_message, get_chat
from db.session import get_db
from models.chat import ChatModel, Message

router = APIRouter()


@router.post("/create", response_model=Chat)
def post_chat(chat: Chat, db=Depends(get_db)):
    new_chat = create_chat(db=db, name=chat.name)
    if new_chat:
        return new_chat
    raise HTTPException(
        status_code=400, detail="Creazione della chat non andata a buon fine"
    )


@router.post("/send", response_model=MessageResponse)
def send_message(message: MessageResponse, db=Depends(get_db)):
    new_message = create_message(
        id=message.id_, text=message.text, chat=message.chat_uuid, db=db
    )
    if new_message:
        return new_message
    raise HTTPException(status_code=400, detail="Impossibile inviare il messaggio")


@router.get("/{id}", response_model=Chat)
def find_chat(id: str, db=Depends(get_db)):
    chat = get_chat(id=id, db=db)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat non trovata")
