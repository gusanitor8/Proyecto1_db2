from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from Connection.DBConnection import get_books, get_book_by_name, get_book_image, get_author_by_id, add_author, \
    update_author, delete_author, add_book
from utils.JsonEncoder import JSONencoder
from data_classes.data_classes import Authors, Books
import json

responses_router = APIRouter()


@responses_router.get("/libros/{page}")
def get_books_(page: int):
    result = get_books(page)
    result = json.dumps(result, indent=4, cls=JSONencoder)

    return Response(content=result, status_code=200)


@responses_router.get("/libros/get/{title}")
def get_book_by_name_(title: str):
    result = get_book_by_name(title)

    if result:
        result = json.dumps(result, indent=4, cls=JSONencoder)
        return Response(content=result, status_code=200)
    else:
        return Response(content=None, status_code=404)


@responses_router.get("/libros/img/{title}")
def get_book_image_(title: str):
    image = get_book_image(title)

    return Response(
        content=image,
        media_type=f"image/jpeg",
        status_code=200
    )

@responses_router.post("/libros/add/{author_id}")
def add_book_(book: Books, author_id: str):
    res = add_book(book, author_id)
    if res:
        return Response(content="Success, author added", status_code=200)
    else:
        return Response(content="Error, author not added", status_code=500)

@responses_router.post("/authors/add")
def add_author_(author: Authors):
    res = add_author(author)
    if res:
        return Response(content="Success, author added", status_code=200)
    else:
        return Response(content="Error, author not added", status_code=500)


@responses_router.put("/authors/update/{author_id}")
def update_author_(author: Authors, author_id: str):
    flag = update_author(author, author_id)
    if flag:
        return Response(content="Success, author updated", status_code=200)
    else:
        return Response(content="Error, author not updated", status_code=500)


@responses_router.get("/authors/get/{author_id}")
def get_author_by_id_(author_id: str):
    result = get_author_by_id(author_id)

    if result:
        result = json.dumps(result, indent=4, cls=JSONencoder)
        return Response(content=result, status_code=200)
    else:
        return Response(content=None, status_code=404)


@responses_router.delete("/authors/delete/{author_id}")
def delete_author_(author_id: str):
    flag = delete_author(author_id)
    if flag:
        return Response(content="Success, author deleted", status_code=200)
    else:
        return Response(content="Error, author not deleted", status_code=500)


