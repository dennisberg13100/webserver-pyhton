import http.server
import socketserver
from router import Router


PORT = 8000

with socketserver.TCPServer(("", PORT), Router) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()