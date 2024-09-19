from fastapi import APIRouter, HTTPException, Depends, status
from schemas.user import User
from api.v1.services.user_service import UserService
from api.v1.auth_service import get_current_user_email
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()
user_service = UserService()


@router.post("/registrazione")
async def registrazione(user: User):
    result = user_service.register_user(user)
    if result:
        return {"message": "Utente registrato con successo"}
    raise HTTPException(status_code=400, detail="Registrazione fallita")


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = user_service.authenticate_user(form_data)
    if token:
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Autenticazione fallita",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.get("/profile")
async def get_profile(email: str = Depends(get_current_user_email)):
    user = user_service.get_user_by_email(email)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Utente non trovato")

