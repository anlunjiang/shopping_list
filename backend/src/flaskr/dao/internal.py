from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class SHOPPING_LIST(Base):
    __tablename__ = "SHOPPING_LIST"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    CREATED = Column(DateTime)
    LAST_UPDATED = Column(DateTime)
    NAME = Column(String(length=50))
