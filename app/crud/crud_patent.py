from sqlalchemy.orm import Session
from models.patent import PatentModel
from db.session import SessionLocal


def create_patent(
        uuid: int, 
        name: str, 
        status: str,
        description: str,
        db: Session = SessionLocal()
        ):
    try:
        db_patent = PatentModel(uuid=uuid, name=name, status=status, description=description)
        db.add(db_patent)
        db.commit()
        return db_patent
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
