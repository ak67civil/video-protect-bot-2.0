from pyrogram import Client, filters
from config import ADMIN_ID
from database import cursor, conn


@Client.on_message(filters.command("addclient") & filters.user(ADMIN_ID))
async def add_client(client, message):

    try:
        client_id = int(message.command[1])
        channel_id = int(message.command[2])

        cursor.execute(
            "INSERT INTO clients (client_id, channel_id) VALUES (?, ?)",
            (client_id, channel_id)
        )
        conn.commit()

        await message.reply_text("✅ Client Added Successfully")

    except:
        await message.reply_text("Usage:\n/addclient client_id channel_id")


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
