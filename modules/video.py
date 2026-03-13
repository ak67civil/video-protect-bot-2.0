
from pyrogram import Client, filters
from database import cursor, conn
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# -------------------------------
# ADD STUDENT
# -------------------------------
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


# -------------------------------
# LIST STUDENTS
# -------------------------------
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


# -------------------------------
# SAVE VIDEO FROM CHANNEL
# -------------------------------
@Client.on_message(filters.video & filters.channel)
async def save_video(client, message):

    file_id = message.video.file_id
    client_id = message.chat.id

    cursor.execute(
        "INSERT INTO videos (file_id, client_id) VALUES (?, ?)",
        (file_id, client_id)
    )
    conn.commit()


# -------------------------------
# WATCH VIDEO
# -------------------------------
@Client.on_message(filters.command("watch"))
async def watch_video(client, message):

    user_id = message.from_user.id

    cursor.execute(
        "SELECT * FROM students WHERE user_id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        return await message.reply_text("❌ You are not authorized")

    cursor.execute("SELECT file_id FROM videos")
    videos = cursor.fetchall()

    if not videos:
        return await message.reply_text("No videos available")

    for v in videos:
        await message.reply_video(v[0])
