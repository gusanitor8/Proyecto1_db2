from pymongo.mongo_client import MongoClient
from gridfs import GridFS
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
DB_NAME = "Testing"
URI = os.getenv('ENV_DB_URI')
client = MongoClient(URI, tlsCAFile=certifi.where())
db = client[DB_NAME]
fs = GridFS(db)
