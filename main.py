from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

import modules.start
import modules.admin
import modules.video

app = Client(
    "coursebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

app.run()
