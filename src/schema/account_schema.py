from typing import List
from pydantic import BaseModel, EmailStr

from src.schema.user_schema import UserBase




class AccountBase(BaseModel):
    email: EmailStr
    password: str
    users: List[UserBase]

class AccountCreate(BaseModel):
    pass

class Account(BaseModel):
    account_id: str

    class config():
        orm_mode = True;