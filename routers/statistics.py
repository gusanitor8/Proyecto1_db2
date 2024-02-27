from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from Connection.agregations import get_top_authors
from utils.JsonEncoder import JSONencoder
import json
from src.plotting import plot_top_authors

statistics_router = APIRouter()


@statistics_router.get("/top_authors/img/", tags=["statistics"])
def get_top_authors_plt():
    res = get_top_authors()
    buffer = plot_top_authors(res)

    return Response(
        content=buffer.getvalue(),
        media_type="image/png",
        status_code=200)


@statistics_router.get("/top_authors/json/", tags=["statistics"])
def get_top_authors_json():
    res = get_top_authors()
    res = json.dumps(res, indent=4, cls=JSONencoder)
    return Response(
        content=res,
        media_type="application/json",
        status_code=200)