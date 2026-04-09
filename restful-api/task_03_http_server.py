#!/usr/bin/python3
#  http. server:
#  http is a library with tools to work with the HTTP protocol
#  server is a submodule of http

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #  all the self. comes from BaseHTTPRequestHandler
        #  self.path stores the URL the client requested
        #  self.send_response sends HTTP srtatus code
        #  self.send_header sends HTTP headers
        #  self.end_headers tells server "Im done sending headers"
        #  > you call this before sending the body  
        #  self.wfile is a writeable stream used to send data 
        #  self.wfile.write sends the response body
        #  200 is the response code when the server succesfully received request
        #  404 is when it failed
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple APPI built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())

port=8000

if __name__ == "__main__":
    server_address =("0.0.0.0", port)
    httpd = HTTPServer(server_address, APIHandler)
    print(f"Server running on http://{server_address[0]}:{port}")
    httpd.serve_forever()
