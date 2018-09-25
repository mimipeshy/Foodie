import jwt
from instance import config
from functools import wraps
from flask import jsonify, request, make_response


def token_required(f):
    """checks for authenticated users with valid tokens"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token is None:
            return make_response(jsonify({"message": "Please sign-up and login"}), 401)
        try:
            data = jwt.decode(token, config['SECRET_KEY'])
        except:
            return make_response(jsonify({"message": 'Token is invalid'}), 401)
        return f(*args, **kwargs)

    return decorated()


def admin_required(f):
    """checks for authenticated admins with valid tokens"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided and ensures the user is an admin"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if token is None:
            return make_response(jsonify({"message": "Please login and signup"}))
        try:
            data = jwt.decode(token, config['SECRET_KEY'])
            admin = data['is_admin']
        except:
            return make_response(jsonify({"message": "Invalid token in header"}), 401)
        if not admin:
            return make_response(
                jsonify({"message": "you are not authorized to perform this function as a non-admin user"}), 401)

        return f(*args, **kwargs)

        return decorated
