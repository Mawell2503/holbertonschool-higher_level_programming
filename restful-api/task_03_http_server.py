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
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello this is your API!!".encode())

        elif self.path == "/data":
            data ={
                "name": "John",
                "age": 30,
                "city": "New York"
                }
            self.send_response()
            self.send_header()
            self.end_headers()
            self.wfile.write()

        elif self.path == "/status":
            self.send_response()
            self.send_header()
            self.end_headers()
            self.wfile.write()

        elif self.path == "/info":
            