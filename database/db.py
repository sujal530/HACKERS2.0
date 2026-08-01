import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'aspire_ai.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enables dict-like column access
    return conn