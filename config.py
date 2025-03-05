import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "replace_this_with_a_secure_key"
    # For local development using SQLite:
    SQLALCHEMY_DATABASE_URI = "sqlite:///portfolio.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
