from pydantic import BaseModel
from typing import List, Optional


class Books(BaseModel):
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
