#!/usr/bin/env python3
"""a module on session
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """a class on SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """this function creates a session
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        value = self.user_id_by_session_id.get(session_id)
        return value

    def current_user(self, request=None) -> User:
        """returns a User instance based on a cookie value
        """
        user_id = self.session_cookie(request)
        user_id_1 = self.user_id_for_session_id(user_id)
        return User.get(user_id_1)
