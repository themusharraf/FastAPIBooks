# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import crud

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user


@app.post("/books/", response_model=schemas.BookResponse)
def create_book(user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book, user_id=user_id)
    return db_book
