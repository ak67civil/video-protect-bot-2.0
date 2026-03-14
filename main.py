from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH, UPLOAD_CHANNEL, INDEX_CHANNEL, LOG_CHANNEL

bot = Client(
    "video-protect-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# START COMMAND
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🤖 Bot Working!")

# VIDEO UPLOAD HANDLER
@bot.on_message(filters.chat(UPLOAD_CHANNEL) & filters.video)
async def upload_video(client, message):

    caption = message.caption if message.caption else "🎬 New Video"

    try:
        sent = await client.send_video(
            chat_id=INDEX_CHANNEL,
            video=message.video.file_id,
            caption=caption,
            protect_content=True
        )
    except Exception as e:
        print("VIDEO SEND ERROR:", e)

    await client.forward_messages(
        chat_id=LOG_CHANNEL,
        from_chat_id=UPLOAD_CHANNEL,
        message_ids=[message.id]
    )

    print("✅ Video Indexed")

print("🚀 Bot Started")

bot.run()
