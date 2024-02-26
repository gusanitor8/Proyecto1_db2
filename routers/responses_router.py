from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from Connection.DBConnection import get_books
from utils.JsonEncoder import JSONencoder
import json

responses_router = APIRouter()


@responses_router.get("/libros/{page}")
def get_books_(page: int):
    result = get_books(page)
    result = json.dumps(result, indent=4, cls=JSONencoder)

    return Response(content=result, status_code=200)
