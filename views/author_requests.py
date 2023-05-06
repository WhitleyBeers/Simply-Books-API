import sqlite3
import json
from models import Author

AUTHORS = [
    {
        "id": 1,
        "email": "molly@doyle.com",
        "first_name": "Molly",
        "last_name": "Doyle",
        "image": "url placeholder",
        "favorite": True
    },
    {
        "id": 2,
        "email": "lemony@snicket.com",
        "first_name": "Lemony",
        "last_name": "Snicket",
        "image": "url placeholder",
        "favorite": False
    },
    {
        "id": 3,
        "email": "stephenie@meyer.com",
        "first_name": "Stephenie",
        "last_name": "Meyer",
        "image": "url placeholder",
        "favorite": False
    }
]

def get_all_authors():
    """returns all authors
    """
    with sqlite3.connect("./simply_books.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * from Authors
        """)
        authors = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            author = Author(row['id'], row['email'], row['first_name'],
                            row['last_name'], row['image'], row['favorite'])
            authors.append(author.__dict__)

    return authors


def get_single_author(id):
    """gets a single author
    Args:
        id (int): id of author
    """
    with sqlite3.connect("./simply_books.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT * from Authors
        WHERE id = ?
        """, ( id, ))
        data = db_cursor.fetchone()
        author = Author(data['id'], data['email'], data['first_name'],
                        data['last_name'], data['image'], data['favorite'])
        return author.__dict__


def get_favorite_authors(favorite):
    """gets authors where favorite = True
    """
    with sqlite3.connect("./simply_books.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT * from Authors
        WHERE favorite IS ?
        """, ( favorite, ))
        authors = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            author = Author(row['id'], row['email'], row['first_name'],
                            row['last_name'], row['image'], row['favorite'])
            authors.append(author.__dict__)

    return authors


def create_author(author):
    """creates an author
    """
    max_id = AUTHORS[-1]["id"]
    new_id = max_id + 1
    author["id"] = new_id
    AUTHORS.append(author)
    return author

def delete_author(id):
    """deletes an author using the id
    """
    author_index = -1
    for index, author in enumerate(AUTHORS):
        if author["id"] == id:
            author_index = index
    if author_index >= 0:
        AUTHORS.pop(author_index)

def update_author(id, new_author):
    """updates author using id
    """
    for index, author in enumerate(AUTHORS):
        if author["id"] == id:
            AUTHORS[index] = new_author
            break
