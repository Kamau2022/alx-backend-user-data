#!/usr/bin/env python3
"""a module on personal data
"""
import bcrypt

def hash_password(password):
    """a function to encrypt password
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
