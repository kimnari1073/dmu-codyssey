# database.py
from contextlib import contextmanager
import sqlite3

DATABASE_URL = "example.db"


@contextmanager
def get_db():
    db = None
    try:
        db = sqlite3.connect(DATABASE_URL)
        db.row_factory = sqlite3.Row
        print("📌 DB CONNECTED")
        yield db
    finally:
        if db:
            db.close()
            print("🔌 DB CLOSED")
