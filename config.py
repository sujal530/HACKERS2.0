import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aspire_ai_hackathon_secret_key'
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''  # Put your MySQL password here
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'aspire_ai'