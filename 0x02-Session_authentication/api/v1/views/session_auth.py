#!/usr/bin/env python3
""" Module of session views
"""
from flask import Blueprint, request
from flask import jsonify, abort
from models.user import User
from api.v1.views import app_views
import os
from typing import Tuple
session_auth_blueprint = Blueprint('session_auth', __name__)


@session_auth_blueprint.route('/auth_session/login',
                              methods=['POST'])
@session_auth_blueprint.route('/api/v1/auth_session/login',
                              methods=['POST'])
def login() -> Tuple[str, int]:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    """user = User()
    namelist = user.search({"email": email})
    if len(namelist) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    if user.is_valid_password(password) and len(namelist) != 0:
        from api.v1.app import auth
        session_id = auth.create_session(self.user_id)
        cookie_name = os.getenv('SESSION_NAME')
        return User.to_json(session_id)
    """
    users = User.search({'email': email})
    if len(users) == 0:
        return ({"error": "no user found for this email"}), 404
    if users[0].is_valid_password(password):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401
