import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, API_ID, API_HASH, UPLOAD_CHANNEL, INDEX_CHANNEL, LOG_CHANNEL, ADMIN_ID

bot = Client(
    "video-protect-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Bot Working!")

@bot.on_message(filters.chat(UPLOAD_CHANNEL) & filters.video)
async def upload_video(client, message):

    caption = message.caption if message.caption else "🎬 New Video"

    sent = await client.send_video(
        chat_id=INDEX_CHANNEL,
        video=message.video.file_id,
        caption=caption,
        protect_content=True
    )

    await client.forward_messages(
        LOG_CHANNEL,
        UPLOAD_CHANNEL,
        message.id
    )

print("🚀 Bot Started")

async def main():
    await bot.start()
    await idle()

from pyrogram import idle

asyncio.run(main())
