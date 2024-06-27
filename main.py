from fastapi import FastAPI, Depends
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


@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger.info("Root endpoint was called")
    db_user = crud.create_user(db=db, user=user)
    return db_user


@app.post("/books/", response_model=schemas.BookResponse)
def create_book(user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book, user_id=user_id)
    return db_book
