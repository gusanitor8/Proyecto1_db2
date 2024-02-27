from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
DB_NAME = "Testing"
URI = os.getenv('ENV_DB_URI')
client = MongoClient(URI, tlsCAFile=certifi.where())
db = client[DB_NAME]


def get_books(page: int, page_size: int = 10):
    collection = db["books"]
    return list(collection.find().skip(page * page_size).limit(page_size))


def get_book_by_name(name: str):
    collection = db["books"]
    return collection.find_one({"title": name})



