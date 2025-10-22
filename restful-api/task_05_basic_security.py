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
    return jsonify({"error": "Invalid username or password"}), 401


@app.route('/jwt-protected', methods=["GET"])
@jwt_required() # requires valid JWT token to access endpoint
def jwt_protected_api():
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only_api():
    user_identity = get_jwt_identity() # e.g. this will return "user1"
    current_user = users.get(user_identity) # this will return the user dictionary
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Override error handling to return 401
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
