# File: app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow React Native to call the API

# Sample data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET request: Fetch users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# POST request: Add a user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
