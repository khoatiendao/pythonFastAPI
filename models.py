import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
# from typing import List, Optional
# from uuid import UUID, uuid4
from enum import Enum
from src.database.database import Base

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4), unique=True, index=True)
    first_name= Column(String)
    last_name = Column(String)
    gender=Column(SQLAlchemyEnum(Gender), nullable=False)
    email = Column(String, unique=True ,index=True)
    password = Column(String)
    role = Column(SQLAlchemyEnum(Role), nullable=False)
    # school = relationship("School", back_populates="teacher")

class School(Base):
    __tablename__ = "schools"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4), unique=True, index=True)
    name_school = Column(String)
    name_class = Column(Integer)
    teacher_id = Column(String, ForeignKey('users.id'))
    # teacher = relationship("User", back_populates="Schools")

