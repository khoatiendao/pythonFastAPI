from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    pass

class UserCreate(BaseModel):
    account_id: str

class UserUpdate(BaseModel):
    username: str
    gender: Optional[str]
    birthday: date
    interest: str
    major: str

class User(BaseModel):
    user_id: str

    class config():
        orm_mode = True;