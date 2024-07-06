from sqlalchemy.orm import Session
from models import User, Book
from werkzeug.security import generate_password_hash
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Create a new book
def create_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_book = Book(
        title=book.title,
        language=book.language,
        isbn=book.isbn,
        pages=book.pages,
        user_id=user_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_all_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user_update.username
        db_user.email = user_update.email
        db_user.is_active = user_update.is_active
        if user_update.password:
            db_user.password = generate_password_hash(user_update.password)
        db.commit()
        db.refresh(db_user)
    return db_user


def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.title = book_update.title
        db_book.language = book_update.language
        db_book.isbn = book_update.isbn
        db_book.pages = book_update.pages
        db.commit()
        db.refresh(db_book)
    return db_book
