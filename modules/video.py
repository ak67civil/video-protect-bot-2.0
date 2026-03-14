from pyrogram import Client, filters
from database import cursor, conn
from config import UPLOAD_CHANNEL
from datetime import datetime


# ---------------------------------
# SAVE VIDEO FROM UPLOAD CHANNEL
# ---------------------------------
@Client.on_message(filters.video & filters.chat(int(UPLOAD_CHANNEL)))
async def save_video(client, message):

    file_id = message.video.file_id
    client_id = message.chat.id

    cursor.execute(
        "INSERT INTO videos (file_id, client_id) VALUES (?, ?)",
        (file_id, client_id)
    )

    conn.commit()


# ---------------------------------
# WATCH VIDEOS
# ---------------------------------
@Client.on_message(filters.command("watch"))
async def watch_video(client, message):

    user_id = message.from_user.id

    # Check user
    cursor.execute(
        "SELECT client_id, expiry_date FROM students WHERE user_id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        return await message.reply_text("❌ You are not authorized.")

    client_id = user[0]
    expiry_date = user[1]

    today = datetime.now().strftime("%Y-%m-%d")

    if expiry_date < today:
        return await message.reply_text("⛔ Your access has expired.")

    # Get videos
    cursor.execute(
        "SELECT file_id FROM videos WHERE client_id=?",
        (client_id,)
    )

    videos = cursor.fetchall()

    if not videos:
        return await message.reply_text("No lectures available yet.")

    for v in videos:

        await message.reply_video(
            v[0],
            caption="🎬 Lecture"
        )

        # Save analytics
        cursor.execute(
            "INSERT INTO analytics (user_id, file_id) VALUES (?, ?)",
            (user_id, v[0])
        )

    conn.commit()
