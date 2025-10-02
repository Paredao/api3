# criar uma api com sqlite para cadastrar, listar e buscar produto pelo id

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy.engine import URL
from typing import List
from pydantic import BaseModel

app=FastAPI()

DATABASE_URL="sqlite:///db.sqlite3"

engine=create_engine(
    DATABASE_URL, connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

