from fastapi import APIRouter, HTTPException, Depends, status
import crud.crud_user
from models.user import UserModel
from db.session import get_db
from schemas.user import User
from api.v1.services.user_service import UserService
from api.v1.auth_service import get_current_user_email
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import crud


router = APIRouter()
user_service = UserService()


@router.post("/registrazione")
async def registrazione(user: User,
                        db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    print(user)
    return db_user


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    token = user_service.authenticate_user(form_data, db)
    if token:
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Autenticazione fallita",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.get("/profile")
async def get_profile(email: str = Depends(get_current_user_email)):
    user = crud.crud_user.get_user (email)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Utente non trovato")

