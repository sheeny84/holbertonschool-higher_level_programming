#!/usr/bin/python3
import http.server
import json


class BasicHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Send response status code
            self.send_response(200)

            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send response body
            message = "<h1>Hello, this is a simple API!</h1>"
            self.wfile.write(bytes(message, "utf8"))
        elif self.path == '/data':
            # Send response status code
            self.send_response(200)

            # Send headers
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Send response body
            my_dict = {"name": "John", "age": 30, "city": "New York"}
            message = json.dumps(my_dict)
            self.wfile.write(bytes(message, "utf8"))
        elif self.path == '/status':
            # Send response status code
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')


def run(server_class=http.server.HTTPServer,
        handler_class=BasicHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
