from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
import database

from models import Category
from schemas import CategoryCreate, CategoryResponse, CategoryUpdate

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

@router.get("/{id}", response_model=CategoryResponse)
async def get_category(id :int, db: Session = Depends(database.get_db)):
    db_category = db.get(Category, id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")
    return db_category

@router.get("/", response_model=list[CategoryResponse])
async def get_categories(db: Session = Depends(database.get_db)):
    statement = select(Category)
    result = db.execute(statement)
    return result.scalars().all()

@router.put("/{id}", response_model=CategoryResponse)
async def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(database.get_db),
    #current_user: str = Depends(get_current_user)
):
    db_category = db.get(Category, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")

    db_category.name = category.name

    db.commit()
    db.refresh(db_category)

    return db_category

@router.delete("/{id}", response_model=CategoryResponse)
async def delete_category(
    category_id: int,
    db: Session = Depends(database.get_db),
    #current_user: str = Depends(get_current_user)
    ):
    db_category = db.get(Category, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")

    db.delete(db_category)

    db.commit()

    return db_category