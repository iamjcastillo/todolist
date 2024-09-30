# app/database.py
from contextvars import ContextVar
from typing import Annotated

from fastapi import Depends
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://user:password@postgres-db:5432/dbname")

Base = declarative_base()

db_session: ContextVar[Session] = ContextVar("db_session")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
DBSessionDependency = Annotated[Session, Depends(get_db)]
