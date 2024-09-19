from sqlalchemy.orm import Session
from ..models.patent import PatentModel
from ..db.session import get_db
from fastapi import Depends

def get_patents(db: Session = Depends(get_db)):
    return db.query(PatentModel).all()

def create_patent(
        uuid: int, 
        name: str, 
        status: str,
        description: str,
        db: Session
        ):
    try:
        db_patent = PatentModel(uuid=uuid, name=name, status=status, description=description)
        db.add(db_patent)
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def remove_patent(
        name: str,
        db: Session
):
    try:
        db.query(PatentModel).filter(PatentModel.name == name).delete()
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()


