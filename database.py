import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

# Clients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
client_id INTEGER PRIMARY KEY,
channel_id INTEGER
)
""")

# Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
user_id INTEGER,
client_id INTEGER
)
""")

# Videos table
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
file_id TEXT,
client_id INTEGER
)
""")

# Analytics table
cursor.execute("""
CREATE TABLE IF NOT EXISTS analytics(
user_id INTEGER,
file_id TEXT
)
""")

conn.commit()
