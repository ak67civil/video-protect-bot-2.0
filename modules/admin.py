from pyrogram import Client, filters
from config import ADMIN_ID
from database import cursor, conn
from datetime import datetime, timedelta


@Client.on_message(filters.command("adduser") & filters.user(ADMIN_ID))
async def add_user(client, message):

    try:
        user_id = int(message.command[1])
        days = int(message.command[2])
    except:
        return await message.reply_text(
            "Usage:\n/adduser user_id days"
        )

    expiry = datetime.now() + timedelta(days=days)

    cursor.execute(
        "INSERT OR REPLACE INTO students (user_id, expiry_date) VALUES (?,?)",
        (user_id, expiry.strftime("%Y-%m-%d"))
    )

    conn.commit()

    await message.reply_text("✅ User added successfully")
