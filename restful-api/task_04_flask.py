#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


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
    new_user = request.get_json()
    if new_user.get("username", None) is None:
        return {"error": "Username is required"}
    users.update(new_user)
    return f"New user added: {jsonify(new_user)}"


if __name__ == "__main__":
    app.run()
