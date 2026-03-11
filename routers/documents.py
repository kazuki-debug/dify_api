from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database

from models import Document
from schemas import DocumentCreate

router = APIRouter()

@router.post("/", response_model=DocumentCreate)
async def create_category(
    document: DocumentCreate,
    db: Session = Depends(database.get_db),
    #current_user: models.User = Depends(auth.get_current_user)
):
    new_category = Document(**document.model_dump())
    print(new_category)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

