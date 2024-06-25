from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    password = Column(String)

    book = relationship("Book", back_populates='users')


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    language = Column(String(20), nullable=True)
    year = Column(TIMESTAMP, default=datetime.utcnow)
    isbn = Column(String(20), unique=True)
    pages = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates='books')
