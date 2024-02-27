from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from Connection.DBConnection import get_books, get_book_by_name
from utils.JsonEncoder import JSONencoder
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




