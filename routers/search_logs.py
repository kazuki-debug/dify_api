from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
import database

from models import Searchlog
from schemas import LogCreate, LogResponse

router = APIRouter()

@router.post("/", response_model=LogCreate)
async def create_log(
    search_log: LogCreate,
    db: Session = Depends(database.get_db),
    #current_user: models.User = Depends(auth.get_current_user)
):
    new_search_log = Searchlog(**search_log.model_dump())
    new_search_log.created_at = datetime.now()

    db.add(new_search_log)
    db.commit()
    db.refresh(new_search_log)
    return new_search_log

@router.get("/{id}", response_model=LogResponse)
async def get_log(id :int, db: Session = Depends(database.get_db)):
    db_log = db.get(Searchlog, id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="指定された本は見つかりません")
    return db_log

@router.get("/", response_model=list[LogResponse])
async def get_logs(db: Session = Depends(database.get_db)):
    statement = select(Searchlog)
    result = db.execute(statement)
    return result.scalars().all()