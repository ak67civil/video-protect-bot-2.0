import sqlite3

# Create database connection
conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

# -------------------------------
# CLIENTS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
    client_id INTEGER PRIMARY KEY,
    channel_id INTEGER
)
""")

# -------------------------------
# STUDENTS TABLE (with expiry)
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    user_id INTEGER PRIMARY KEY,
    client_id INTEGER,
    expiry_date TEXT
)
""")

# -------------------------------
# VIDEOS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id TEXT,
    client_id INTEGER
)
""")

# Index for faster queries
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_client
ON videos(client_id)
""")

# -------------------------------
# ANALYTICS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS analytics(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_id TEXT,
    watch_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Save changes
conn.commit()
