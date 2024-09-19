from sqlalchemy.orm import Session
from models.patent import PatentModel
from schemas.patent import PatentList


def create_patent(
        name: str, 
        status: str,
        description: str,
        db: Session
        ):
    try:
        db_patent = PatentModel(name=name, status=status, description=description)
        db.add(db_patent)
        db.commit()
        db.refresh(db_patent)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
        return db_patent


def get_all_patents(
        
) -> PatentList:
    pass


