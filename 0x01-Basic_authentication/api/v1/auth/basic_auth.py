#!/usr/bin/env python3
"""basic authorization
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """a class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """returns the Base64 part of the Authorization
           header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if isinstance(authorization_header, str):
            first_word = authorization_header.split()[0]
            if first_word == 'Basic':
                return authorization_header.split()[1]
            else:
                return None
