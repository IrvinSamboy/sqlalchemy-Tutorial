from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)

