from sqlalchemy.orm import Session
from models.user import UserModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt


def authenticate_user(db: Session, username: str, password: str):
    db_user = db.query(UserModel).filter(UserModel.username == username).first()
    
    if db_user and verify_password(password, db_user.password):
        return create_access_token(data={"sub": db_user.email})
    
    return None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
