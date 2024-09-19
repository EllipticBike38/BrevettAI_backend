# from google_patent_scraper import scraper_class #type: ignore
from fastapi import APIRouter, Depends
from typing import List, Optional
from crud.crud_patent import create_patent
from sqlalchemy.orm import Session
from db.session import get_db
import requests #type: ignore
from ..utils.patents_utils import find_patent_by_id



router = APIRouter()

@router.get("/get_patents/{patent_id}")
def get_patents(
    patent_id: str,
):
    try:
        patents = find_patent_by_id(patent_id)
        print(patents)
        return patents
    except ValueError:
        return 404
    # response = requests.get("https://patents.google.com/xhr/query?url=q%3D(moka)%26oq%3Dmoka")
    # print(response.json())

