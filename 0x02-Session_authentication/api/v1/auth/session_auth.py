#!/usr/bin/env python3
"""a module on session
"""
from api.v1.auth.auth import Auth
import uuid


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
