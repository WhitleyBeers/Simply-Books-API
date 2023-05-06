import sqlite3
import json
from models import Book

BOOKS = [
    {
        "id": 1,
        "title": "Bloodshed",
        "image": "url placeholder",
        "price": 16.00,
        "sale": True,
        "description": "A full-length novel focused on the favorite Masked Men. We like to " \
        "believe monsters don't exist, even in the moonlit streets of a place like " \
        "Salem, Massachusetts. But they're very real... and very human. ..."
    },
    {
        "id": 2,
        "title": "The Grim Grotto",
        "image": "url placeholder",
        "price": 12.99,
        "sale": False,
        "description": "The Grim Grotto is the eleventh novel in the " \
        "children's book series A Series of Unfortunate Events by Lemony Snicket."
    }
]

def get_all_books():
    """returns all books
    """
    with sqlite3.connect("./simply_books.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * from Books
        """)
        books = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            book = Book(row['id'], row['title'], row['image'],
                        row['price'], row['sale'], row['description'],
                        row['author_id'])
            books.append(book.__dict__)

    return books


def get_single_book(id):
    """gets a single book
    Args:
        id (int): id of book
    """
    requested_book = None

    for book in BOOKS:
        if book["id"] == id:
            requested_book = book

    return requested_book


def create_book(book):
    """creates a book
    """
    max_id = BOOKS[-1]["id"]
    new_id = max_id + 1
    book["id"] = new_id
    BOOKS.append(book)
    return book


def delete_book(id):
    """deletes an book using the id
    """
    book_index = -1
    for index, book in enumerate(BOOKS):
        if book["id"] == id:
            book_index = index
    if book_index >= 0:
        BOOKS.pop(book_index)


def update_book(id, new_book):
    """updates book using id
    """
    for index, book in enumerate(BOOKS):
        if book["id"] == id:
            BOOKS[index] = new_book
            break
