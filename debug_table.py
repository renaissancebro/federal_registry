import sqlite3
conn = sqlite3.connect("federal_registry.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(federal_register_entries);")
print(cursor.fetchall())

# conn = sqlite3.connect("federal_registry.db")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

for (table_name,) in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    print(f"[✂️] Dropped table: {table_name}")

conn.commit()
conn.close()
