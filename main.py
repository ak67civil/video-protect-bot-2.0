import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import PeerIdInvalid

from config import BOT_TOKEN, API_ID, API_HASH, UPLOAD_CHANNEL, INDEX_CHANNEL, LOG_CHANNEL

bot = Client(
    "video-protect-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🤖 Bot Working!")


@bot.on_message(filters.chat(UPLOAD_CHANNEL) & filters.video)
async def upload_video(client, message):

    caption = message.caption if message.caption else "🎬 New Video"

    try:

        # send video to index channel
        sent = await client.send_video(
            chat_id=INDEX_CHANNEL,
            video=message.video.file_id,
            caption=caption,
            protect_content=True
        )

        # forward to log channel
        await client.forward_messages(
            chat_id=LOG_CHANNEL,
            from_chat_id=UPLOAD_CHANNEL,
            message_ids=message.id
        )

        print("✅ Video Indexed")

    except PeerIdInvalid:
        print("❌ Channel ID invalid or bot not admin")


async def main():
    await bot.start()
    print("🚀 Bot Started")
    await asyncio.Event().wait()


asyncio.run(main())
