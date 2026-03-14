from pyrogram import Client, filters
from config import ADMIN_ID
from database import cursor

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast(client, message):

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast")

    cursor.execute("SELECT user_id FROM students")

    users = cursor.fetchall()

    for user in users:
        try:
            await message.reply_to_message.copy(user[0])
        except:
            pass

    await message.reply_text("✅ Broadcast Completed")
