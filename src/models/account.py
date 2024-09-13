import uuid
from sqlalchemy import Column, String
from src.database.database import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    email = Column(String, unique=True ,index=True)
    password = Column(String)
    users = relationship("User", back_populates="account", uselist=False)