# from typing import List
# import uuid
# from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAlchemyEnum
# from sqlalchemy.orm import relationship
# from enum import Enum
# from src.database.database import Base

# class Gender(str, Enum):
#     male = "Male"
#     female = "Female"

# class Role(str, Enum):
#     admin = "Admin"
#     user = "User"
#     student = "Student"

# class User(Base):
#     __tablename__ = "users"

#     id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
#     first_name= Column(String)
#     last_name = Column(String)
#     gender=Column(SQLAlchemyEnum(Gender), nullable=False)
#     email = Column(String, unique=True ,index=True)
#     password = Column(String)
#     role = Column(SQLAlchemyEnum(Role), nullable=False)
#     school_id = Column(String, ForeignKey('schools.id'))
#     school = relationship("School", back_populates="teachers")

# class School(Base):
#     __tablename__ = "schools"

#     id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
#     name_school = Column(String)
#     name_class = Column(String)
#     # teacher_id = Column(String, ForeignKey('users.id'))
#     teachers = relationship("User", back_populates="school")
    

