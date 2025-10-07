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
    if username not in users:
        return jsonify({"error": "User not found"})
    return users.get(username)


@app.post("/add_user")
def add_user_api():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    if data["username"] in users:
        return jsonify({"error": "Username already exists"}), 400
    username = data["username"]
    users[username] = data
    user_info = data.copy()
    user_info.pop("username", None)
    return jsonify({"message": f"User added ", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
