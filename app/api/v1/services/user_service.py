from api.v1.models.user import UserModel, PatentModel
from api.db.session import SessionLocal
from api.core.security import verify_password, create_access_token
from fastapi import FastAPI, Depends, HTTPException,status
class UserService:
    def __init__(self):
        self.db = SessionLocal()

    def register_user(self, user):
        existing_user = session.query(models.User).filter_by(email=user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        encrypted_password = get_hashed_password(user.password)

        new_user = models.User(username=user.username, email=user.email, password=encrypted_password )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return True

    def authenticate_user(self, user):
        db_user = self.db.query(UserModel).filter(UserModel.username == user.username).first()
        if db_user and verify_password(user.password, db_user.password):
            return create_access_token(data={"sub": db_user.username})
        return None
    
    def logout(self):
        # Implementa la logica per il logout
        return True

    def send_message(self, message):
        # Implementa la logica per inviare un messaggio al chatbot
        return "Messaggio inviato"

    def get_conversations(self):
        # Recupera le conversazioni dal database
        return []

    def get_chat_names(self):
        # Recupera i nomi delle chat
        return []

    def get_completed_patents(self):
        # Recupera tutti i brevetti completati
        return self.db.query(PatentModel).filter(PatentModel.status == "completed").all()

    def get_pending_patents(self):
        # Recupera tutti i brevetti da fare
        return self.db.query(PatentModel).filter(PatentModel.status == "pending").all()
