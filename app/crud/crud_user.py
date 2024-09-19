from sqlalchemy.orm import Session
from models.user import UserModel
from db.session import SessionLocal


def create_user(
        email: str, 
        username: str, 
        password: str,
        db: Session = SessionLocal()
        ):
    try:
        db_user = UserModel(email=email, username=username, password=password)
        db.add(db_user)
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()


def update_user(email: str, 
                new_username: str = None, 
                new_password: str = None,
                db: Session = SessionLocal()
                ):
    try:
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if user:
            if new_username:
                user.username = new_username
            if new_password:
                user.password = new_password
            db.commit()
    finally:
        db.close()


def get_user(email: str, db: Session = SessionLocal()):
    try:
        return db.query(UserModel).filter(UserModel.email == email).first()
    finally:
        db.close()
