from google_patent_scraper import scraper_class #type: ignore
from fastapi import APIRouter, Depends
from typing import List, Optional
from ....crud.crud_patent import create_patent
from sqlalchemy.orm import Session
from ....db.session import get_db
import requests #type: ignore

router = APIRouter()

@router.get("/get_patents")
def get_patents(
):


    response = requests.get("https://patents.google.com/xhr/query?url=q%3D(moka)%26oq%3Dmoka")
    print(response.json())

