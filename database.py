 import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

# students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    user_id INTEGER PRIMARY KEY,
    expiry_date TEXT
)
""")

# videos table
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id TEXT
)
""")

# analytics
cursor.execute("""
CREATE TABLE IF NOT EXISTS analytics(
    user_id INTEGER,
    file_id TEXT
)
""")

conn.commit()
