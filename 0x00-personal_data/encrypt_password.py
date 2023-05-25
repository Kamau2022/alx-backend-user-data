#!/usr/bin/env python3
"""a module on personal data
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """a function to encrypt password
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks whether the password is valid
    """
    userBytes = password.encode('utf-8')
    result = bcrypt.checkpw(userBytes, hashed_password)
    return result
