import http.server
from html_builder import html_builder

class Router(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': self.handle_index,
            '/hello': self.handle_hello,
            '/goodbye': self.handle_goodbye
        }

        if self.path in routes:
            routes[self.path]()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
    
    def handle_index(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html_content = html_builder()
        self.wfile.write(html_content.encode())

    def handle_hello(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World!")

    def handle_goodbye(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Goodbye, World!")
