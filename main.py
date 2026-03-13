from pyrogram import Client
from config import *

import modules.start
import modules.admin
import modules.video

app = Client(
    "course_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

print("Bot Started 🚀")

app.run()
