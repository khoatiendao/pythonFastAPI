from types import new_class
from typing import Annotated, List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
import models
from src.schema.schema import SchoolUpdate, UserBase, UserUpdate, SchoolBase
from src.database.database import Base
from models import School, User
from src.config.config_dotenv import settings
from src.database.database import engine
from src.database.database import db_dependency


def create_table():
    models.Base.metadata.create_all(bind=engine)

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

@app.post("/api/v1/user")
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(
        first_name = user.first_name,
        last_name = user.last_name,
        gender = user.gender,
        email = user.email,
        password = user.password,
        role = user.role)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail=f"Please check all information"
        )
    return db_user

# Get all user
@app.get("/api/v1/users")
async def get_users(db: db_dependency):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=404,
            detail=f"Not found" 
        )
    return users;

# Get one user
@app.get("/api/v1/users/{user_id}")
async def get_users_id(user_id: str, db: db_dependency):
    result = db.query(models.User).filter(models.User.id == user_id).first()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} not found"
        )
    return result;

# DELETE user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: str, db: db_dependency):
    result = db.query(models.User).filter(models.User.id == user_id).first()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} not found"
        )
    db.delete(result)
    db.commit()
    return {"message" : f"Delete user with id: {user_id} successfull"}
    

# UPDATE user
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: str, user_update: UserUpdate ,db: db_dependency):
    find_userId = db.query(models.User).filter(models.User.id == user_id).first()
    if not find_userId:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} not found"
        )
    
    find_userId.first_name = user_update.first_name
    find_userId.last_name = user_update.last_name
    find_userId.gender = user_update.gender
    find_userId.email = user_update.email
    find_userId.password = user_update.password

    db.commit()
    db.refresh(find_userId)
    return find_userId;

# POST school
@app.post("/api/v1/school")
async def create_school(school: SchoolBase, db: db_dependency):
    db_school = models.School(
        name_school = school.name_school,
        name_class = school.name_class
    )
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    for teacher in school.teachers:
        db_teacher = models.User(
        first_name = teacher.first_name,
        last_name = teacher.last_name,
        gender = teacher.gender,
        email = teacher.email,
        password = teacher.password,
        role = teacher.role,
        school_id = db_school.id)
        db.add(db_teacher)
    db.commit()
    return db_school

@app.get("/api/v1/school")
async def get_school(db: db_dependency):
    result = db.query(models.School).all()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Not found"
        )
    return result;


@app.get("/api/v1/school/{school_id}")
async def get_schoolWithUser(school_id: str ,db: db_dependency):
    result = db.query(models.School).filter(models.School.id == school_id).first()

    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"School id: {school_id} not found"
        )
    return result;

# @app.put("/api/v1/school/{school_id}")
# async def update_school(school_id: str, school_update: SchoolUpdate ,db: db_dependency):
#     result = db.query(models.School).filter(models.School.id == school_id).first()
#     print(result.teachers)

#     if not result:
#         raise HTTPException(
#             status_code=404,
#             detail=f"School id: {school_id} not found"
#         )
#     result.name_school = school_update.name_school
#     result.name_class = school_update.name_class
#     result.teachers = school_update.teachers

#     db.commit()
#     db.refresh(result)
#     return result;

        


    