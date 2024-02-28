from Connection.database import db, fs
from data_classes.data_classes import UserDisplayParams


def get_top_authors():
    collection = db["books"]

    pipeline = [
        {
            "$group": {
                "_id": "$author_id",  # Group by author ID
                "books": {"$sum": 1},  # Count the number of books for each author
            }
        },
        {
            "$sort": {"books": -1}},  # Sort by "books" field in descending order
        {
            "$lookup": {
                "from": "authors",  # Specify the collection to join
                "localField": "_id",  # Field in the "books" collection to join on (author ID)
                "foreignField": "_id",  # Field in the "authors" collection to join on (author ID)
                "as": "author_info"  # Name for the resulting array of matched documents
            }
        },
        {
            "$unwind": "$author_info"  # Unwind the "author_info" array
        },
        {
            "$project": {
                "_id": 0,  # Exclude the original "_id" field if not needed
                "author_id": "$_id",  # Keep the author ID
                "books": 1,  # Keep the book count
                "author_name": "$author_info.name"  # Access the author name from the joined data
            }
        },
        {
            "$limit": 5  # Limit the results to the top 5 authors
        }
    ]

    results = list(collection.aggregate(pipeline))
    return results


def user_projection(user_params: UserDisplayParams, page: int):
    page_size = 10
    skip = page * page_size

    collection = db["users"]

    filter_field = ""
    if user_params.filter:
        filter_field = user_params.filter.value
    sort_field = user_params.param.value
    sort_order = user_params.sort.value

    pipeline = []

    if filter_field:
        pipeline.append({"$match": {filter_field: {"$exists": True}}})  # Filter documents with specified field

    # Add projection stage only if filter_field is provided
    if filter_field:
        pipeline.append({"$project": {filter_field: 1, "_id": 0}})  # Project only the specified field

    if sort_field:
        sort_direction = 1 if sort_order == 1 else -1
        pipeline.append({"$sort": {sort_field: sort_direction}})

    pipeline.append({"$skip": skip})
    pipeline.append({"$limit": page_size})

    cursor = collection.aggregate(pipeline)
    return list(cursor)

def get_author_count():
    collection = db["authors"]
    return collection.count_documents({})


def get_book_count():
    collection = db["books"]
    return collection.count_documents({})
