from types import new_class
from typing import Annotated, List
from uuid import UUID, uuid4
from fastapi import Depends, FastAPI, HTTPException
from src.schema.schema import UserCreate
from src.database.database import Base, SessionLocal, get_async_session
from models import School, User
from src.config.config_dotenv import settings
from src.database.database import engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select





def create_table():
    Base.metadata.create_all(bind=engine)

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

@app.post("/api/v1/user", response_model=UserCreate)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    new_user = User(first_name=user.first_name, 
                    last_name=user.last_name, 
                    gender=user.gender, 
                    email=user.email, 
                    password=user.password,
                    role=user.role)
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


# # Get user
# @app.get("/api/v1/users")
# async def fetch_users():
#     return db;

# @app.get("/api/v1/class")
# async def fetch_class():
#     return db_school;

# @app.get("/api/v1/class/{class_id}")
# async def get_classId(class_id: UUID):
#     for classSchool in db_school:
#         if classSchool.id == class_id:
#             return {
#                 "id" : classSchool.id,
#                 "name_class": classSchool.name_class,
#                 "total_class": classSchool.total_class,
#                 "teacher": classSchool.teacher
#             }
#         raise HTTPException(
#             status_code=400,
#             detail=f"Please check information and fill all"
#         )

# # QUERY
# @app.get("/api/v1/users/{user_id}")
# async def query_user(user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             return {
#                 "id": user.id,
#                 "first_name": user.first_name,
#                 "last_name" : user.last_name,
#                 "middle_name": user.middle_name,
#                 "gender" : user.gender,
#                 "roles" : user.roles
#             }
#         raise HTTPException(
#             status_code=404,
#             detail=f"User with id: {user_id} is not found"
#         )


# # POST user
# @app.post("/api/v1/users")
# async def register_user(user: User):
#     db.append(user)
#     return {"id": user.id}

# @app.post("/api/v1/class")
# async def create_class(school: School):
#     db.append(school)
#     return {"message" : "Create class successfull"}

# # DELETE user
# @app.delete("/api/v1/users/{user_id}")
# async def delete_user(user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             db.remove(user)
#             return 
#         raise HTTPException(
#             status_code=404,
#             detail=f"user with id: {user_id} is not exists"
#         )
    

# # UPDATE user
# @app.put("/api/v1/users/{user_id}")
# async def update_user(user_update: UserUpdateRequest, user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             if user_update.first_name is not None:
#                 user.first_name = user_update.first_name
#             if user_update.last_name is not None:
#                 user.last_name = user_update.last_name
#             if user_update.middle_name is not None:
#                 user.middle_name = user_update.middle_name
#             if user_update.gender is not None:
#                 user.gender = user_update.gender
#             if user_update.roles is not None:
#                 user.roles = user_update.roles

#             return {"message" : "Update Success"}
        
#     raise HTTPException (
#         status_code=404,
#         detail=f"user with id: {user_id} is not exsists"
#     )