import sqlite3

# CONNECT DATABASE
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
# STUDENTS TABLE
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    user_id INTEGER,
    client_id INTEGER
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

# SAVE CHANGES
conn.commit()
