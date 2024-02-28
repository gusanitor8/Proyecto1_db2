from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Books(BaseModel):
    _id: Optional[str] = None
    title: str
    genre: List[str]
    publication_date: str
    ISBN: str
    available_copies: int
    reviews: List[dict]
    author_id: Optional[str] = None
    cover_image: Optional[str] = None


class Authors(BaseModel):
    name: str
    email: str
    birth_date: str
    biography: str
    nationality: str


class ParamEnum(Enum):
    BORROWED_BOOKS = "borrowed_books"
    NAME = "name"
    EMAIL = "email"
    USERNAME = "username"


class SortEnum(Enum):
    DESC = -1
    ASC = 1
    AS_IS = 0


class UserDisplayParams(BaseModel):
    sort: SortEnum
    filter: Optional[ParamEnum] = None
    param: ParamEnum


