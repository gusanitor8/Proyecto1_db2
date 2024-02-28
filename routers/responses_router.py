from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from Connection.crud_ops import get_books, get_book_by_name, get_book_image, get_author_by_id, add_author, \
    update_author, delete_author, add_book, update_book, get_author_by_keyword, delete_book
from utils.JsonEncoder import JSONencoder
from Connection.agregations import get_author_count, get_book_count
from data_classes.data_classes import Authors, Books
import json

responses_router = APIRouter()


@responses_router.get("/libros/count", tags=["books"])
def get_books_count_():
    count = get_book_count()
    return JSONResponse(content={"count": count}, status_code=200)


@responses_router.get("/libros/{page}", tags=["books"])
def get_books_(page: int):
    result = get_books(page)
    result = json.dumps(result, indent=4, cls=JSONencoder)

    return Response(content=result, media_type="application/json", status_code=200)


@responses_router.get("/libros/get/{title}", tags=["books"])
def get_book_by_name_(title: str):
    result = get_book_by_name(title)

    if result:
        result = json.dumps(result, indent=4, cls=JSONencoder)
        return Response(content=result, media_type="application/json", status_code=200)
    else:
        return Response(content=None, status_code=404)


@responses_router.get("/libros/img/{title}", tags=["books"])
def get_book_image_(title: str):
    image = get_book_image(title)

    return Response(
        content=image,
        media_type="image/jpeg",
        status_code=200
    )


@responses_router.post("/libros/add/{author_id}", tags=["books"])
def add_book_(book: Books, author_id: str):
    res = add_book(book, author_id)
    if res:
        return Response(content="Success, author added", status_code=200)
    else:
        return Response(content="Error, author not added", status_code=500)


@responses_router.delete("/libros/delete/{book_id}", tags=["books"])
def delete_book_(book_id: str):
    flag = delete_book(book_id)
    if flag:
        return Response(content="Success, book deleted", status_code=200)
    else:
        return Response(content="Error, book not deleted", status_code=500)


@responses_router.put("/libros/update/{book_id}", tags=["books"])
def update_book_(book: Books, book_id: str):
    flag = update_book(book, book_id)
    if flag:
        return Response(content="Success, author updated", status_code=200)
    else:
        return Response(content="Error, author not updated", status_code=500)


@responses_router.get("/authors/count", tags=["authors"])
def get_authors_count_():
    count = get_author_count()
    return JSONResponse(content={"count": count}, status_code=200)


@responses_router.post("/authors/add", tags=["authors"])
def add_author_(author: Authors):
    res = add_author(author)
    if res:
        return Response(content="Success, author added", status_code=200)
    else:
        return Response(content="Error, author not added", status_code=500)


@responses_router.get("/authors/get/{keyword}", tags=["authors"])
def get_author_by_keyword_(keyword: str):
    result = get_author_by_keyword(keyword)
    result = json.dumps(result, indent=4, cls=JSONencoder)

    if result:
        return Response(content=result, media_type="application/json", status_code=200)
    else:
        return Response(content=None, status_code=404)


@responses_router.put("/authors/update/{author_id}", tags=["authors"])
def update_author_(author: Authors, author_id: str):
    flag = update_author(author, author_id)
    if flag:
        return Response(content="Success, author updated", status_code=200)
    else:
        return Response(content="Error, author not updated", status_code=500)


@responses_router.get("/authors/get/{author_id}", tags=["authors"])
def get_author_by_id_(author_id: str):
    result = get_author_by_id(author_id)

    if result:
        result = json.dumps(result, indent=4, cls=JSONencoder)
        return Response(content=result, status_code=200)
    else:
        return Response(content=None, status_code=404)


@responses_router.delete("/authors/delete/{author_id}", tags=["authors"])
def delete_author_(author_id: str):
    flag = delete_author(author_id)
    if flag:
        return Response(content="Success, author deleted", status_code=200)
    else:
        return Response(content="Error, author not deleted", status_code=500)
