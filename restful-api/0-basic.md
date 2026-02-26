#  What is HTTP and HTTPS
The foundation of data exchange on the web, transmitting data in a secure or insecure way
The protocol used to transfer data between clients and web server.

HHTP > HyperText Transfer Protocol
        > "Sending a postcard(anyone can read it)"
        > insecure data(not encrypted)
        > uses port:80
        > faster
        > Stateless(each request is independent)

HTTPS > HyperText Transfer Protocol Secure
        > "Sending a sealed envelop(private and secure)"
        > uses SSL/TLS to secure data(encrypts data)
            -SSL
            > It is a security protocol created to encrypt communication between a browser(client) and a web server

            -TSL
            > Improved and secure version of SSL(more secured and modern)

        > protects sensitive data
        > uses port 443
        > slower due to encrption
#  Basic structure of HTTP request and responses.
Your Browser sends an HTTP request to the server, and the server sends back an HTTP response(part of house(HTML, CSS, images, JSON,etc.)).
    -HTML(bricks)
    > HyperText Markup Language
    > It defines the structure of webpage("Think of it as the skeleton of a website")

    -CSS(paint and decoration)
    > Cascading Style Sheets
    > It controls the appearance of HTML("Think of it as the clothes and styling of the skeleton")

    -images(furniture)
    > Images are media files sent by the server to the browser

    -JSON(Information about owner)
    > JavaScript Object Notation
    > It is a data format, not a design language
#  Common HTTP methods and status code
HTTP methods tell the server what action you want to perform on a resource:
    GET/
        > used to fetch data{GET /user}
    POST/
        > creates new data{POST /user}
    PUT/
        > used to replace/update a full resources{PUT /user/5}
    PATCH/
        > used to update only some fields
    DELETE/
        > used to delete a resource

Status code tells you what happened after the request:
    1xx -> informational(rarely used directly)

    2xx -> success
        200 OK - everything worked
        201 Created - Resource successfully created
        204 Content - Success but no response body
    
    3xx -> redirection
        301 - Moved permenanently 
        302 - Found
    
    4xx -> Client Errors (your Fault)
        400 Bad Request
        401 Unauthorized
        403 Forbidden
        404Not Found

    5xx -> Server Error
        500 Server Error