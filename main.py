from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.error_handler import ErrorHandler
from middlewares.cors_middleware import get_origins
from routers.responses_router import responses_router
from dotenv import load_dotenv
import os

app = FastAPI()
app.title = "Bookify API"

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Error Handler
app.add_middleware(ErrorHandler)
app.include_router(responses_router)