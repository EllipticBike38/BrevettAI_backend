from fastapi import Depends
from models.user import UserModel
from models.patent import PatentModel
from api.core.security import verify_password, create_access_token


class UserService:
    def __init__(self) -> None:
        pass

    def register_user(self, user, db):
        db_user = UserModel(username=user.username, password=user.password, email=user.email)
        db.add(db_user)
        db.commit()
        db.close()
        return True

    def authenticate_user(self, user, db):
        db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
        if db_user and verify_password(user.password, db_user.password):
            return create_access_token(data={"sub": db_user.username})
        return None

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
