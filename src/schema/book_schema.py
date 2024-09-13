from pydantic import BaseModel


class BookBase(BaseModel):
    name_book: str
    image_book: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BaseModel):
    id: str

    class config():
        orm_mode = True;

class UpdateBook(BaseModel):
    name_book: str
    image_book: str
    author: str