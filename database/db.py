import mysql.connector
from mysql.connector import Error

from config import Config


def get_db_connection():
    """
    Returns a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            autocommit=True
        )

        return connection

    except Error as error:
        print(f"Database Connection Error: {error}")
        return None


def close_db_connection(connection):
    """
    Safely closes the database connection.
    """

    if connection is not None and connection.is_connected():
        connection.close()