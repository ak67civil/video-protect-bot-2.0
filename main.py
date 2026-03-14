import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, API_ID, API_HASH, UPLOAD_CHANNEL, INDEX_CHANNEL, LOG_CHANNEL, ADMIN_ID

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

bot = Client(
    "video-protect-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# START COMMAND
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Welcome!\n\nSend /watch <video_id> to watch video."
    )

# VIDEO UPLOAD LISTENER
@bot.on_message(filters.chat(UPLOAD_CHANNEL) & filters.video)
async def upload_video(client, message):

    video = message.video.file_id
    caption = message.caption if message.caption else "🎬 New Video"

    # SEND VIDEO TO INDEX CHANNEL
    sent = await client.send_video(
        chat_id=INDEX_CHANNEL,
        video=video,
        caption=caption,
        protect_content=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▶️ WATCH", url=f"https://t.me/{(await client.get_me()).username}?start={sent.id}")]]
        )
    )

    # SEND LOG COPY
    await client.forward_messages(
        LOG_CHANNEL,
        UPLOAD_CHANNEL,
        message.id
    )

# WATCH COMMAND
@bot.on_message(filters.command("watch"))
async def watch_video(client, message):

    try:
        video_id = int(message.command[1])
    except:
        return await message.reply_text("❌ Invalid video id")

    msg = await client.get_messages(INDEX_CHANNEL, video_id)

    await client.copy_message(
        chat_id=message.chat.id,
        from_chat_id=INDEX_CHANNEL,
        message_id=video_id,
        protect_content=True
    )

print("🚀 Bot Started")

bot.run()
