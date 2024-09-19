from app.models.chat import ChatModel, Message
from sqlalchemy.orm import Session


def create_chat(id: str, name: str, db: Session):
    try:
        db_chat = ChatModel(id_=id, name=name)
        db.add(db_chat)
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()


def get_chat(id: str, db: Session):
    try:
        chat = db.query(ChatModel).filter(ChatModel.uuid == id).one()
        return chat
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()


def create_message(id: str, text: str, chat: str, db: Session):
    try:
        db_chat = get_chat(id=chat, db=Session)
        db_message = Message(id_=id, text=text, order=len(db_chat.messages))
        db.add(db_message)
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
