#!/usr/bin/env python3
"""a module on data
"""
from typing import List
import re
import os
import logging
import mysql.connector
patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """that returns the log message obfuscated
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """a function that connects to a database.
    """
    host = os.environ.get("PERSONAL_DATA_DB_HOST")
    database = os.environ.get("PERSONAL_DATA_DB_NAME")
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD")
    conn = mysql.connector.connect(
                     host=host,
                     user=user,
                     password=password,
                     database=database,
        )
    return conn
