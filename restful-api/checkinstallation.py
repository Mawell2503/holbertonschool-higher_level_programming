import requests

#  this line sends a HTTP request to github; "Hey send me your data"
response = requests.get("https://api.github.com")
#  this prints the HTTP status code returned by the server, github in this case
#  200 -> success
#  404 -> not found
#  500 -> server error
#  403 -> forbidden
print(response.status_code)