from fastapi import APIRouter
from schemas.user import Message, Chat, Patent
from api.v1.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/manda-messaggio")
async def manda_messaggio(message: Message):
    response = user_service.send_message(message)
    return {"response": response}

@router.get("/recupera-conversazioni")
async def recupera_conversazioni():
    conversations = user_service.get_conversations()
    return {"conversazioni": conversations}

@router.get("/recupera-nomi-chat")
async def recupera_nomi_chat():
    chat_names = user_service.get_chat_names()
    return {"nomi_chat": chat_names}

@router.get("/recupera-brevetti-fatti")
async def recupera_brevetti_fatti():
    completed_patents = user_service.get_completed_patents()
    return {"brevetti_fatti": completed_patents}

@router.get("/recupera-brevetti-da-fare")
async def recupera_brevetti_da_fare():
    pending_patents = user_service.get_pending_patents()
    return {"brevetti_da_fare": pending_patents}
