from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

import database

from models import Document
from schemas import DocumentCreate, DocumentResponse

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

@router.get("/{id}", response_model=DocumentResponse)
async def get_document(id :int, db: Session = Depends(database.get_db)):
    db_document = db.get(Document, id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")
    return db_document

@router.get("/", response_model=list[DocumentResponse])
async def get_documents(db: Session = Depends(database.get_db)):
    statement = select(Document)
    result = db.execute(statement)
    return result.scalars().all()

@router.put("/{id}", response_model=DocumentResponse)
async def update_document(
    document_id: int,
    document: DocumentCreate,
    db: Session = Depends(database.get_db),
    #current_user: str = Depends(get_current_user)
):
    db_document = db.get(Document, document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")

    db_document.category_id = document.category_id
    db_document.title = document.title
    db_document.content = document.content

    db.commit()
    db.refresh(db_document)

    return db_document

@router.delete("/{id}", response_model=DocumentResponse)
async def delete_document(
    document_id: int,
    db: Session = Depends(database.get_db),
    #current_user: str = Depends(get_current_user)
    ):
    db_document = db.get(Document, document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")

    db.delete(db_document)

    db.commit()

    return db_document