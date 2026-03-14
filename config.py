import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")

UPLOAD_CHANNEL = int(os.getenv("UPLOAD_CHANNEL", 0))
INDEX_CHANNEL = int(os.getenv("INDEX_CHANNEL", 0))

ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
