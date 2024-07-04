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
