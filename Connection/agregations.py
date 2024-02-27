from Connection.database import db, fs


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
