#!/usr/bin/env python3
""" Module of session views
"""
from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views
from os import getenv
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if len(users) == 0:
        return ({"error": "no user found for this email"}), 404
    for instance in users:
        from api.v1.app import auth
        if not instance.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        sessionId = auth.create_session(instance.id)
        res = jsonify(instance.to_json())
        res.set_cookie(getenv("SESSION_NAME"), sessionId)
        return res


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete() -> Tuple[str, int]:
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    destroy = auth.destroy_session(request)
    if destroy is False:
        abort(404)
    else:
        return jsonify({}), 200
