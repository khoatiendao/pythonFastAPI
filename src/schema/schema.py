from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import List, Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    gender: Optional[str]
    email: EmailStr
    password: str
    role: Optional[str]

class schoolCreate(BaseModel):
    name_school: str
    name_class: str
    teacher_id: UUID

