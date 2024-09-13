import uuid
from sqlalchemy import Column, ForeignKey, String, Table
from src.database.database import Base

user_books = Table(
    'user_books', Base.metadata,
    Column('user_id', ForeignKey('users.user_id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True)
)

# class User_Book(Base):
#     __tablename__ = "userBooks"

#     id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
#     Column('user_id', ForeignKey('users.user_id'), primary_key=True)
#     Column('book_id', ForeignKey('books.id'), primary_key=True)