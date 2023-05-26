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

    def get_db() - > mysql.connector.connection.MySQLConnection:
        """this function returns a connector to the database
        """
        mydb = mysql.connector.connect(
         host=os.environ.get('PERSONAL_DATA_DB_HOST'),
         user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
         password=os.environ.get('PERSONAL_DATA_DB_PASSWORD'),
         database=os.environ.get('PERSONAL_DATA_DB_NAME')
         )
        return mydb
