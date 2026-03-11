from database import Base
from sqlalchemy import Column, Integer, VARCHAR, DATETIME, Text

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR, index=True)
    created_at = Column(DATETIME)

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    title = Column(VARCHAR, index=True)
    content = Column(Text)
    created_at = Column(DATETIME)