from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ("127.0.0.1", 8000)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Server running at http://127.0.0.1:8000")

httpd.serve_forever()