#!/usr/bin/python3

#  Flask > creates the web application server
#  jsonify > formats Python data as JSON for responses
#  request >accesses incoming HTTP request data
from flask import Flask, jsonify, request

#  creates an WAO for the current module and stores it in app
app = Flask(__name__)

#  storage for users.
users = {}

#  Root end-point.
#  Flask equivalent of self.path == "/"
@app.route("/")
def home():
    return "Welcome to the Flask API!"

#  End-point to return all usernames
#  Flask equivalent of self.path == "/data"
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

#  End-point for status
#  Flask equivalent of self.path == "/status"
@app.route("/status")
def status():
    return jsonify({"status": "OK"})

#  End-point to get a specific user by username
#  Flask equivalent of self.path == "/users/<username>"
@app.route("/users/<username>")
def get_user(username):
    user = user.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

#  End-point to add a new user via POST
#  Flask equivalent of self.path == "/add_user"
#  Flask equivalent of self.command == "POST"
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:

        #  Flask equiavalent of:
        #  self.send_response(400)
        #  self.send_header("Content-Type", "application/json")
        #  self.end_headers()
        #  self.wfile.write(b'{"error": "Invalid JSON"}')
        return jsonify({"error": "Invalid JSON"}), 400
    
    #  Flask equivalent of:
    #  import json
    #  length = int(self.headers.get("Content-Length", 0))
    #  body = self.rfile.read(length)
    #  data = json.loads(body)
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if not username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user":users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
