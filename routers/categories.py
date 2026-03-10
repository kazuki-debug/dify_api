from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database

from models import Category
from schemas import CategoryCreate

router = APIRouter()

@router.post("/", response_model=CategoryCreate)
async def create_category(
    category: CategoryCreate,
    db: Session = Depends(database.get_db),
    #current_user: models.User = Depends(auth.get_current_user)
):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

