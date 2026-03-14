from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import UPLOAD_CHANNEL, INDEX_CHANNEL, LOG_CHANNEL
from database import cursor, conn
from datetime import datetime


# -----------------------------
# AUTO INDEX VIDEO
# -----------------------------
@Client.on_message(filters.video & filters.chat(int(UPLOAD_CHANNEL)))
async def auto_index(client, message):

    file_id = message.video.file_id

    # Send to index channel
    await client.send_video(
        chat_id=int(INDEX_CHANNEL),
        video=file_id,
        caption="📚 New Lecture",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "▶️ Watch Lecture",
                        callback_data=f"watch_{file_id}"
                    )
                ]
            ]
        )
    )

    # Send copy to log channel
    await client.send_video(
        chat_id=int(LOG_CHANNEL),
        video=file_id,
        caption="📥 Video logged"
    )

    cursor.execute(
        "INSERT INTO videos (file_id) VALUES (?)",
        (file_id,)
    )

    conn.commit()


# -----------------------------
# WATCH VIDEO
# -----------------------------
@Client.on_callback_query(filters.regex("watch_"))
async def watch_video(client, callback):

    user_id = callback.from_user.id
    file_id = callback.data.split("_")[1]

    cursor.execute(
        "SELECT expiry_date FROM students WHERE user_id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        return await callback.answer(
            "❌ You are not authorized",
            show_alert=True
        )

    expiry = user[0]
    today = datetime.now().strftime("%Y-%m-%d")

    if expiry < today:
        return await callback.answer(
            "⛔ Your access expired",
            show_alert=True
        )

    await client.send_video(
        chat_id=user_id,
        video=file_id,
        caption="🎬 Lecture",
        protect_content=True
    )

    cursor.execute(
        "INSERT INTO analytics (user_id, file_id) VALUES (?,?)",
        (user_id, file_id)
    )

    conn.commit()

    await callback.answer("📥 Sending lecture...")
