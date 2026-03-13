from pyrogram import Client, filters
from database import cursor, conn


@Client.on_message(filters.command("adduser"))
async def add_user(client, message):

    try:
        user_id = int(message.command[1])
        client_id = message.from_user.id

        cursor.execute(
            "INSERT INTO students (user_id, client_id) VALUES (?, ?)",
            (user_id, client_id)
        )
        conn.commit()

        await message.reply_text("✅ Student Added")

    except:
        await message.reply_text("Usage:\n/adduser user_id")


@Client.on_message(filters.command("users"))
async def list_users(client, message):

    client_id = message.from_user.id

    cursor.execute(
        "SELECT user_id FROM students WHERE client_id=?",
        (client_id,)
    )

    data = cursor.fetchall()

    if not data:
        return await message.reply_text("No students found")

    text = "👨‍🎓 Students List\n\n"

    for x in data:
        text += f"{x[0]}\n"

    await message.reply_text(text)
