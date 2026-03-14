import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

# CLIENTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
    client_id INTEGER PRIMARY KEY,
    channel_id INTEGER
)
""")

# STUDENTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    user_id INTEGER PRIMARY KEY,
    client_id INTEGER
)
""")

# VIDEOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id TEXT,
    client_id INTEGER
)
""")

cursor.execute(
    "CREATE INDEX IF NOT EXISTS idx_client ON videos(client_id)"
)

# ANALYTICS
cursor.execute("""
CREATE TABLE IF NOT EXISTS analytics(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_id TEXT,
    watch_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
