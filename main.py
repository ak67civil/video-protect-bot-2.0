from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

import modules.start
import modules.admin
import modules.video
import modules.watch
import modules.broadcast

app = Client(
    "video-protect-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Bot Started Successfully")

app.run()
