from types import new_class
from typing import Annotated, List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from src.schema.userBook_schema import UserBookBase
from src.schema.book_schema import BookBase, UpdateBook
from src.schema.user_schema import UserUpdate
from src.schema.account_schema import AccountBase
import src.models
from src.database.database import Base
from src.config.config_dotenv import settings
from src.database.database import engine
from src.database.database import db_dependency
# from src.utils.validate import validate_password


def create_table():
    src.models.Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.project_name)
    create_table()
    return app;
    
app = start_application()

# Get demo
@app.get("/config")
def read_config():
    return {
        "Database URL": settings.database_url,
    }

@app.get("/")
def home():
    return {"message" : "Hello FastAPI"}

@app.post("/api/v1/account")
async def register(account: AccountBase, db: db_dependency):
    db_account = src.models.Account(
        email = account.email,
        password = account.password,)
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    for user in account.users:
        db_user = src.models.User(
            account_id = db_account.id
        )
        db.add(db_user)
    db.commit()

    if not db_account:
        raise HTTPException(
            status_code=400,
            detail=f"Please check all information"
        )
    return db_account

# Get all user
@app.get("/api/v1/account")
async def get_users(db: db_dependency):
    account = db.query(src.models.Account).all()
    if not account:
        raise HTTPException(
            status_code=404,
            detail=f"Not found" 
        )
    return account;

# UPDATE user
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: str, user_update: UserUpdate ,db: db_dependency):
    find_userId = db.query(src.models.User).filter(src.models.User.user_id == user_id).first()
    if not find_userId:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} not found"
        )
    
    find_userId.username = user_update.username
    find_userId.gender = user_update.gender
    find_userId.birthday = user_update.birthday
    find_userId.interest = user_update.interest
    find_userId.major = user_update.major

    db.commit()
    db.refresh(find_userId)
    return find_userId;



# POST book
@app.post("/api/v1/book")
async def create_book(book: BookBase, db: db_dependency):
    db_book = src.models.Book(
        name_book = book.name_book,
        image_book = book.image_book,
        author = book.author
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/api/v1/book")
async def get_book(db: db_dependency):
    result = db.query(src.models.Book).all()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Not found"
        )
    return result;


@app.get("/api/v1/book/{book_id}")
async def get_bookWithId(book_id: str ,db: db_dependency):
    result = db.query(src.models.Book).filter(src.models.Book.id == book_id).first()

    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"School id: {book_id} not found"
        )
    return result;

@app.put("/api/v1/book/{book_id}")
async def update_book(book_id: str, book_update: UpdateBook ,db: db_dependency):
    result = db.query(src.models.Book).filter(src.models.Book.id == book_id).first()

    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"School id: {book_id} not found"
        )
    result.name_school = book_update.name_school
    result.name_class = book_update.name_class
    result.teachers = book_update.teachers

    db.commit()
    db.refresh(result)
    return result;

@app.post("/api/v1/savebook")
async def save_book(savebook: UserBookBase, db: db_dependency):
    user = db.query(src.models.User).filter(src.models.User.user_id == savebook.user_id).first()
    book = db.query(src.models.Book).filter(src.models.Book.id == savebook.book_id).first()
    print(book)

    if not user or not book:
        raise HTTPException(
            status_code=400,
            detail=f"Something wrong about save books"
        )
    
    user.book.append(book)


    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user" : savebook.user_id, "book" : savebook.book_id};

# # Get one user
# @app.get("/api/v1/users/{user_id}")
# async def get_users_id(user_id: str, db: db_dependency):
#     result = db.query(models.User).filter(models.User.id == user_id).first()
#     if not result:
#         raise HTTPException(
#             status_code=404,
#             detail=f"user with id: {user_id} not found"
#         )
#     return result;

# # DELETE user
# @app.delete("/api/v1/users/{user_id}")
# async def delete_user(user_id: str, db: db_dependency):
#     result = db.query(models.User).filter(models.User.id == user_id).first()
#     if not result:
#         raise HTTPException(
#             status_code=404,
#             detail=f"user with id: {user_id} not found"
#         )
#     db.delete(result)
#     db.commit()
#     return {"message" : f"Delete user with id: {user_id} successfull"}
        


    