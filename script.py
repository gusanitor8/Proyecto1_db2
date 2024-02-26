import os

from pymongo import MongoClient
from gridfs import GridFS
from certifi import where
from faker import Faker
import random
from datetime import datetime

# fake data
fake = Faker()

# database info
client = MongoClient(
    "mongodb+srv://gon21438:12345@cluster0.7y13bzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tlsCAFile=where())
db = client["Testing"]
collection_books = db["books"]
collection_authors = db["authors"]
collection_users = db["users"]
fs = GridFS(db)

# data generation
BOOKS_NUM = 1000
AUTHORS_NUM = 500
USER_NUM = 100

books_ids = []
authors_ids = []
grid_ids = []


def make_reviews(review_num: int):
    reviews = []
    for _ in range(review_num):
        review = {
            "reviewer": fake.name(),
            "comment": fake.text(),
            "rating": fake.random_int(min=1, max=5)
        }
        reviews.append(review)

    return reviews


def make_author():
    test_author = {
        "name": fake.name(),
        "email": fake.email(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=100).strftime("%Y-%m-%d"),
        "biography": fake.text(),
        "nationality": fake.country()
    }

    return test_author


def make_book():
    test_book = {
        "title": fake.sentence(),
        "genre": fake.word(),
        "publication_date": datetime.isoformat(fake.date_time()),
        "ISBN": fake.isbn13(),
        "available_copies": fake.random_int(min=0, max=50),
        "reviews": make_reviews(fake.random_int(min=0, max=10))
    }
    return test_book


def make_user():
    test_user = {
        "name": fake.name(),
        "email": fake.email(),
        "username": fake.user_name(),
    }
    return test_user


def upload_images():
    filenames = os.listdir("images")
    filepath = "images/"

    for filename in filenames:
        with open(filepath + filename, "rb") as f:
            file_data = f.read()

        grid_id = fs.put(file_data, filename=filename)
        grid_ids.append(grid_id)


def upload_authors():
    # insert authors
    with client.start_session() as session:
        with session.start_transaction():
            print("transaction began")
            try:
                for _ in range(AUTHORS_NUM):
                    author = make_author()
                    authors_ids.append(collection_authors.insert_one(author, session=session).inserted_id)
                print("authors uploaded")
                print(authors_ids)
                print()

            except Exception as e:
                print(e)
                session.abort_transaction()
            else:
                session.commit_transaction()
                print("Data inserted successfully")


def upload_books():
    # insert books
    with client.start_session() as session:
        with session.start_transaction():
            print("books transaction began")
            try:
                for _ in range(BOOKS_NUM):
                    book = make_book()
                    book["author_id"] = fake.random_element(authors_ids)
                    book["cover_image"] = fake.random_element(grid_ids)
                    books_ids.append(collection_books.insert_one(book, session=session).inserted_id)
            except Exception as e:
                print(e)
                session.abort_transaction()
            else:
                session.commit_transaction()
                print("Books data inserted successfully")


def upload_users():
    # insert users
    with client.start_session() as session:
        with session.start_transaction():
            print("users transaction began")
            try:
                for _ in range(USER_NUM):
                    user = make_user()
                    borrowed_books = random.sample(books_ids, k=fake.random_int(min=0, max=5))
                    user["borrowed_books"] = borrowed_books
                    collection_users.insert_one(user, session=session)
            except Exception as e:
                print(e)
                session.abort_transaction()
            else:
                session.commit_transaction()
                print("Users data inserted successfully")


def run():
    upload_images()
    upload_authors()
    upload_books()
    upload_users()


run()
