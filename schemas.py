from pydantic import BaseModel
import datetime

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(CategoryCreate):
    id: int
    #completed: bool
    #owner_id: int

    class config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    name: str

class DocumentCreate(BaseModel):
    category_id: int
    title: str
    content: str

class DocumentResponse(DocumentCreate):
    id: int
    
    class config:
        from_attributes = True
