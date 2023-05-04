from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views import get_all_authors, get_all_books, get_all_author_books
from views import get_single_author, get_single_book, get_single_author_books
from views import create_author, create_book, create_author_book
from views import delete_author, delete_book, delete_author_book
from views import update_author

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """parses the url
        """
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)


    def _set_headers(self, status):
        """sets the status code, Content-Type, and Access-Control-Allow-Origin
        headers on the response
        Args: status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Acess-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handles GET requests to the server
        """
        self._set_headers(200)
        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "authors":
            if id is not None:
                response = get_single_author(id)
            else:
                response = get_all_authors()

        elif resource == "books":
            if id is not None:
                response = get_single_book(id)
            else:
                response = get_all_books()

        elif resource == "author_books":
            if id is not None:
                response = get_single_author_books(id)
            else:
                response = get_all_author_books()

        self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        """Handles POST requests to the server
        """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        response = None

        if resource == "authors":
            response = create_author(post_body)
        elif resource == "books":
            response = create_book(post_body)
        elif resource == "author_books":
            response = create_author_book(post_body)

        self.wfile.write(json.dumps(response).encode())


    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)

        if resource == "authors":
            update_author(id, post_body)

        self.wfile.write("".encode())


    def do_DELETE(self):
        """handles delete requests to the server
        """
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)

        if resource == "authors":
            delete_author(id)
        elif resource == "books":
            delete_book(id)
        elif resource == "author_books":
            delete_author_book(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandlesRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
