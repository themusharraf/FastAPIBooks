from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
import logging
import schemas
import crud

app = FastAPI()

# Create a logger object
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("file.log")
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=List[schemas.UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db=db)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
async def get_one_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user


@app.post("/users/", response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger.info("Root endpoint was called")
    db_user = crud.create_user(db=db, user=user)
    return db_user


@app.post("/books/", response_model=schemas.BookResponse)
async def create_book(user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book, user_id=user_id)
    return db_book


@app.get("/books/", response_model=List[schemas.BookResponse])
async def get_books(db: Session = Depends(get_db)):
    books = crud.get_all_books(db=db)
    return books


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
async def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db=db, book_id=book_id)
    if book is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")
    return book
