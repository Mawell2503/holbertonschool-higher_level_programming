#  curl?
It is a command line tool used to senf HTTP request to a server.
    -A way to test APIs
#  basic API request using curl
Specify HTTP Method
    curl -X POST https//example.com/api\
         -H "Content-Type: application/ json"\
         -d'{"name":"Nathanael", "age":20}'


    -X = method
    -H = header
    -d = data(request body)
#  result of common API request
Status Code
Headers
Body(usuallly JSON)