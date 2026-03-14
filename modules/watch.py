from pyrogram import Client, filters
from database import cursor

@Client.on_message(filters.command("watch"))
async def watch(client, message):

    cursor.execute("SELECT file_id FROM videos")

    data = cursor.fetchall()

    if not data:
        return await message.reply_text("No lectures available")

    text = "📚 Available Lectures\n\n"

    for x in data:
        text += f"/start {x[0]}\n"

    await message.reply_text(text)
