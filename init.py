from database import Base, engine
from models import Book, User

Base.metadata.create_all(engine)
