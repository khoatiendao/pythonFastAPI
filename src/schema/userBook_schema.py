from pydantic import BaseModel

class UserBookBase(BaseModel):
    user_id: str
    book_id: str

    class config():
        orm_mode = True;


class UserBookCreate(UserBookBase):
    pass



