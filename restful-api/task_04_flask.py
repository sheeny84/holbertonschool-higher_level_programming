#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data_api():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status_api():
    return "OK"


@app.route("/users/<username>")
def username_api(username):
    user = users.get(username, None)
    if user is None:
        user = {"error", "User not found"}
    return user


@app.post("/add_user")
def add_user_api():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}, 400)
    username = data["username"]
    users[username] = data
    user_info = data.copy()
    user_info.pop("username", None)
    return jsonify({"message": f"User added ", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
