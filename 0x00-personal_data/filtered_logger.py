#!/usr/bin/env python3
"""a module on data
"""
from typing import List
import re
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

    """def get_db() - > mysql.connector.connection.MySQLConnection:
        this function returns a connector to the database
        host = os.getenv('PERSONAL_DATA_DB_HOST', "localhost"),
        user = os.getenv('PERSONAL_DATA_DB_USERNAME', "root"),
        password = os.getenv('PERSONAL_DATA_DB_PASSWORD', ""),
        database = os.getenv('PERSONAL_DATA_DB_NAME')
        mydb = mysql.connector.connect(
               host=host,
               user=user,
               password=password,
               database=database
               )
        return mydb
    """

    def get_db() -> mysql.connector.connection.MySQLConnection:
        """Creates a connector to a database.
        """
        db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
        db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
        db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
        db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
        connection = mysql.connector.connect(
                     host=db_host,
                     port=3306,
                     user=db_user,
                     password=db_pwd,
                     database=db_name,
        )
        return connection
