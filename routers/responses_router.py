from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from Connection.DBConnection import get_books, get_book_by_name, get_book_image, get_author_by_id
from utils.JsonEncoder import JSONencoder
from PIL import Image
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
    image: Image = get_book_image(title)

    return Response(
        content=image,
        media_type=f"image/jpeg",
        status_code=200
    )


@responses_router.get("/authors/get/{author_id}")
def get_author_by_id_(author_id: str):
    result = get_author_by_id(author_id)

    if result:
        result = json.dumps(result, indent=4, cls=JSONencoder)
        return Response(content=result, status_code=200)
    else:
        return Response(content=None, status_code=404)



