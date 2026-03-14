from pyrogram import Client, filters
from config import ADMIN_ID
from database import cursor, conn
from datetime import datetime, timedelta


# -------------------------------
# ADD CLIENT
# /addclient client_id channel_id
# -------------------------------
@Client.on_message(filters.command("addclient") & filters.user(ADMIN_ID))
async def add_client(client, message):

    if len(message.command) != 3:
        return await message.reply_text(
            "Usage:\n/addclient client_id channel_id"
        )

    try:
        client_id = int(message.command[1])
        channel_id = int(message.command[2])

        cursor.execute(
            "INSERT INTO clients (client_id, channel_id) VALUES (?, ?)",
            (client_id, channel_id)
        )

        conn.commit()

        await message.reply_text("✅ Client Added Successfully")

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")


# -------------------------------
# LIST CLIENTS
# /clients
# -------------------------------
@Client.on_message(filters.command("clients") & filters.user(ADMIN_ID))
async def list_clients(client, message):

    cursor.execute("SELECT * FROM clients")
    data = cursor.fetchall()

    if not data:
        return await message.reply_text("No clients found")

    text = "📊 Clients List\n\n"

    for x in data:
        text += f"Client ID: {x[0]}\nChannel: {x[1]}\n\n"

    await message.reply_text(text)


# -------------------------------
# ADD STUDENT WITH EXPIRY
# /adduser user_id days
# -------------------------------
@Client.on_message(filters.command("adduser") & filters.user(ADMIN_ID))
async def add_user(client, message):

    if len(message.command) != 3:
        return await message.reply_text(
            "Usage:\n/adduser user_id days"
        )

    try:
        user_id = int(message.command[1])
        days = int(message.command[2])

        expiry = datetime.now() + timedelta(days=days)
        expiry_date = expiry.strftime("%Y-%m-%d")

        cursor.execute(
            "INSERT OR REPLACE INTO students (user_id, client_id, expiry_date) VALUES (?, ?, ?)",
            (user_id, 1, expiry_date)
        )

        conn.commit()

        await message.reply_text(
            f"✅ User Added\nExpiry: {expiry_date}"
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")


# -------------------------------
# LIST STUDENTS
# /users
# -------------------------------
@Client.on_message(filters.command("users") & filters.user(ADMIN_ID))
async def list_users(client, message):

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if not data:
        return await message.reply_text("No users found")

    text = "👨‍🎓 Students List\n\n"

    for x in data:
        text += f"User ID: {x[0]}\nClient: {x[1]}\nExpiry: {x[2]}\n\n"

    await message.reply_text(text)
