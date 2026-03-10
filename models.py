from database import Base
from sqlalchemy import Column, Integer, VARCHAR, DATETIME

class Category(Base):
    __tabelname__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR, index=True)
    created_at = Column(DATETIME)

