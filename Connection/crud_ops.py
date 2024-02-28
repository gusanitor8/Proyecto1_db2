from data_classes.data_classes import Authors
from data_classes.data_classes import Books, Authors
from bson import ObjectId
from Connection.database import db, fs


def get_books(page: int, page_size: int = 10):
    collection = db["books"]
    return list(collection.find().skip(page * page_size).limit(page_size))


def get_book_by_name(name: str):
    collection = db["books"]
    return collection.find_one({"title": name})


def get_book_image(name: str):
    collection = db["books"]
    book = collection.find_one({"title": name}, {"cover_image": 1})
    book_cover_id = book.get("cover_image")
    # book_cover_id = ObjectId(book_cover_id)

    if book_cover_id:
        try:
            image_data = fs.get(book_cover_id)
            image_data = image_data.read()

            return image_data
        except Exception as e:
            print(f"Error retrieving image: {e}")

    return None


def delete_book(book_id: str):
    collection = db["books"]
    try:
        collection.delete_one({"_id": ObjectId(book_id)})
        return True
    except Exception as e:
        print(f"Error deleting book: {e}")
        return False


def get_author_by_keyword(keyword: str):
    collection = db["authors"]
    pipeline = [
        {
            "$match": {"name": {"$regex": f".*{keyword}.*", "$options": "i"}},
            # Match documents where "name" field contains the keyword (case-insensitive)
        },
        {
            "$limit": 10  # Limit the results to 10
        }
    ]

    results = list(collection.aggregate(pipeline))
    return results


def get_author_by_id(author_id: str):
    collection = db["authors"]
    o_id = ObjectId(author_id)
    return collection.find_one({"_id": o_id})


def add_author(author: Authors):
    try:
        collection = db["authors"]
        author = author.dict()
        collection.insert_one(author)
        return True
    except Exception as e:
        print(f"Error inserting author: {e}")
        return False


def update_author(author: Authors, author_id: str):
    collection = db["authors"]
    try:
        collection.update_one({"_id": ObjectId(author_id)}, {"$set": author.dict()})
        return True
    except Exception as e:
        print(f"Error updating author: {e}")
        return False


def delete_author(author_id: str):
    collection = db["authors"]
    collection_books = db["books"]
    try:
        collection_books.delete_many({"author_id": ObjectId(author_id)})
        collection.delete_one({"_id": ObjectId(author_id)})
        return True
    except Exception as e:
        print(f"Error deleting author: {e}")
        return False


def add_book(book: Books, author_id: str):
    collection = db["books"]
    book = book.dict()
    try:
        book["author_id"] = ObjectId(author_id)
        collection.insert_one(book)
        return True
    except Exception as e:
        print(f"Error inserting book: {e}")
        return False


def update_book(book: Books, book_id: str):
    collection = db["books"]
    book = book.dict()
    book_id = ObjectId(book_id)

    try:
        collection.update_one({"_id": book_id}, {"$set": book})
        return True
    except Exception as e:
        print(f"Error updating book: {e}")
        return False
