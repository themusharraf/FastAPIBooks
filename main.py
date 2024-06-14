import uvicorn
from fastapi import FastAPI
from data import book_db, user_db

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello world"}


@app.get("/books")
async def books():
    return book_db


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return [book for book in book_db if book.get("id") == book_id]


@app.get("/users")
async def users():
    return user_db


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return [user for user in user_db if user.get("id") == user_id]


