from pyrogram import Client, filters
from config import UPLOAD_CHANNEL, INDEX_CHANNEL

@Client.on_message(filters.video & filters.chat(UPLOAD_CHANNEL))
async def handle_video(client, message):

    file_id = message.video.file_id
    title = message.video.file_name

    button = [[
        ("Watch Video", f"https://t.me/{client.me.username}?start={file_id}")
    ]]

    await client.send_message(
        INDEX_CHANNEL,
        f"🎬 {title}\nClick below to watch.",
    )
