#!/usr/bin/env python3
"""basic authorization
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string
           base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            if isinstance(base64_authorization_header, str):
                base64_bytes = base64_authorization_header.encode('utf-8')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('utf-8')
                return message
        except Exception:
            return None
