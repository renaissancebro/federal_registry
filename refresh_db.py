# refresh_db.py
import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "federal_registry.db"))

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE federal_register_entries ADD COLUMN link TEXT")
except sqlite3.OperationalError as e:
    if "duplicate column name" not in str(e):
        raise  # Only suppress if it's the expected error

conn.commit()
conn.close()
print("[✓] Database schema updated.")

