AUTHOR_BOOKS = [
    {
        "id": 1,
        "author_id": 1,
        "book_id": 1
    },
    {
        "id": 2,
        "author_id": 2,
        "book_id": 2
    }
]


def get_all_author_books():
    """gets all author books
    """
    return AUTHOR_BOOKS


def get_single_author_books(id):
    """gets a single author_books
    Args:
        id (int): id of author_books
    """
    requested_author_books = None

    for author_books in AUTHOR_BOOKS:
        if author_books["id"] == id:
            requested_author_books = author_books

    return requested_author_books

def create_author_book(author_book):
    """creates an author book - will figure out how to link it eventually?

    Args:
        author_book (object): link between books and authors
    """
    max_id = AUTHOR_BOOKS[-1]["id"]
    new_id = max_id + 1
    author_book["id"] = new_id
    AUTHOR_BOOKS.append(author_book)
    return author_book
