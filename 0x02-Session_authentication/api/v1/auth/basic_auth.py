#!/usr/bin/env python3
"""basic authorization
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if isinstance(decoded_base64_authorization_header, str):
            k = ':'
            if k not in decoded_base64_authorization_header:
                return (None, None)
            else:
                return (tuple(decoded_base64_authorization_header.split(':')))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """We retrive the user"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = User()
        if user.count() == 0:
            return None
        namelist = user.search({"email": user_email})
        if len(namelist) == 0:
            return None
        else:
            instance = namelist[0]
        if instance.is_valid_password(user_pwd):
            return instance
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        user = self.user_object_from_credentials(email, password)
        return user
