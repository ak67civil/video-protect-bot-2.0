from pyrogram import Client
from config import *

app = Client(
    "course_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message()
async def start(client, message):
    if message.text == "/start":
        await message.reply("Bot is running successfully 🚀")

app.run()
