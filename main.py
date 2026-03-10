from fastapi import FastAPI
import database
import models
from routers import categories

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(categories.router, prefix="/categories", tags=["category"])
