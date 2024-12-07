from typing import Annotated
import os

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine, select

load_dotenv()


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
conn = engine.connect()
print(conn.get_isolation_level())
#
POSTGRES_URL = os.getenv("POSTGRESQL_URL")
print(POSTGRES_URL)

# engine = create_engine(POSTGRES_URL)

#SessionLocal = sessionmaker(autocommit=False ,autoflush=False, bind=engine)
# Base = declarative_base()
# conn = engine.connect()
# print(conn.get_isolation_level())



