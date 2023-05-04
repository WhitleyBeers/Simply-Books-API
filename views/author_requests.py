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
    return AUTHORS


def get_single_author(id):
    """gets a single author
    Args:
        id (int): id of author
    """
    requested_author = None

    for author in AUTHORS:
        if author["id"] == id:
            requested_author = author

    return requested_author


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
