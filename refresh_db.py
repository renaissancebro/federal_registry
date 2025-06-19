# refresh_db.py
import sqlite3
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "federal_registry.db"))

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("ALTER TABLE federalregister_gov_api_v1_documents_rss RENAME TO federal_registry")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("[✓] Existing tables:", cursor.fetchall())
try:
    cursor.execute("ALTER TABLE federal_register_entries ADD COLUMN summary TEXT")
except sqlite3.OperationalError as e:
    if "duplicate column name" not in str(e):
        raise  # Only suppress if it's the expected error

conn.commit()
conn.close()
print("[✓] Database schema updated.")

