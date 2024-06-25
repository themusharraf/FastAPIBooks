from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello world"}


@app.get("/books")
async def books():
    ...


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    ...


@app.get("/users")
async def users():
    ...


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    ...
