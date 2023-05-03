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
    return BOOKS


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
