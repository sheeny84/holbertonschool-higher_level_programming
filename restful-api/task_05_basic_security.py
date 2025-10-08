#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, JWTManager
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)

# Create instance of HTTPBasicAuth class
auth = HTTPBasicAuth()

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "shh"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password":
              generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password":
               generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if username in list(users.keys()) and \
            check_password_hash(user.get("password"), password):
        return username


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def basic_protected_api():
    if auth.current_user():
        return "Basic Auth: Access Granted"
    return jsonify({"error": "Unauthorized"}), 401


@app.route('/login', methods=["POST"])
def login_api():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == verify_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid username or password"}), 400


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwt_protected_api():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    if current_user is None:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify("JWT Auth: Access Granted"), 200


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only_api():
    current_user = users.get(get_jwt_identity())
    print(f"Current user is {current_user}")
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
