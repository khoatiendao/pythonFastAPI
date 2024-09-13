# from pydantic import BaseModel, EmailStr, Field
# from uuid import uuid4
# from typing import List, Optional

# class UserBase(BaseModel):
#     first_name: str
#     last_name: str
#     gender: Optional[str]
#     email: EmailStr
#     password: str
#     role: Optional[str]

#     class config():
#         orm_mode = True;

# class SchoolBase(BaseModel):
#     name_school: str
#     name_class: str
#     teachers: List[UserBase]

#     class config():
#         orm_mode = True;

# class UserUpdate(BaseModel):
#     first_name: str
#     last_name: str
#     gender: Optional[str]
#     email: EmailStr
#     password: str

# class SchoolUpdate(BaseModel):
#     name_school: str
#     name_class: str
#     teachers: List[UserBase]

