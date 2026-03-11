from fastapi import FastAPI
import database
import models
from routers import categories, documents, search_logs

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(categories.router, prefix="/categories", tags=["category"])
app.include_router(documents.router, prefix="/documents", tags=["document"])
app.include_router(search_logs.router, prefix="/search_logs", tags=["search_log"])
