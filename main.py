from fastapi import FastAPI
import database
import models
from routers import categories, documents

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(categories.router, prefix="/categories", tags=["category"])
app.include_router(documents.router, prefix="/documents", tags=["document"])
