from fastapi import APIRouter, HTTPException
from schemas.user import User, Login
from api.v1.services.user_service import UserService


router = APIRouter()
user_service = UserService()


@router.post("/registrazione")
async def registrazione(user: User):
    result = user_service.register_user(user)
    if result:
        return {"message": "Utente registrato con successo"}
    raise HTTPException(status_code=400, detail="Registrazione fallita")


@router.post("/login")
async def login(user: Login):
    token = user_service.authenticate_user(user)
    if token:
        return {"token": token}
    raise HTTPException(status_code=401, detail="Autenticazione fallita")
