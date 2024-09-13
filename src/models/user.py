from enum import Enum
import uuid
from sqlalchemy import Column, Date, ForeignKey, String, Enum as SQLAlchemyEnum
from src.database.database import Base
from sqlalchemy.orm import relationship
from src.models.userBooksSave import user_books


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    username= Column(String)
    gender=Column(SQLAlchemyEnum(Gender))
    birthday = Column(Date)
    interest = Column(String)
    major = Column(String)
    account_id = Column(String, ForeignKey('accounts.id'))
    account = relationship("Account", back_populates="users")
    book = relationship("Book", secondary=user_books, back_populates="user")

    