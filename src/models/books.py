import uuid
from sqlalchemy import Column, String
from src.database.database import Base
from sqlalchemy.orm import relationship
from src.models.userBooksSave import user_books


class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    name_book = Column(String)
    image_book = Column(String)
    author = Column(String)
    user = relationship("User", secondary=user_books, back_populates="book")