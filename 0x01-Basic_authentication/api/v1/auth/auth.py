#!/usr/bin/env python3
""" API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """a class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authentication
        """
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths or path + "/" in excluded_paths:
            return False
        else:
            return True
        if path is None:
            return True

    def authorization_header(self, request=None) -> str:
        """a function to get authorization from a header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        """
        return None
