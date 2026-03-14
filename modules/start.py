from pyrogram import Client, filters
from database import cursor, conn


@Client.on_message(filters.command("start"))
async def start_cmd(client, message):

    user_id = message.from_user.id

    # Check student
    cursor.execute(
        "SELECT * FROM students WHERE user_id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        return await message.reply_text(
            "❌ You are not authorized to use this bot."
        )

    # If start link contains video id
    if len(message.command) > 1:

        file_id = message.command[1]

        await message.reply_video(
            file_id,
            caption="🎬 Enjoy your lecture"
        )

        # Save analytics
        cursor.execute(
            "INSERT INTO analytics (user_id, file_id) VALUES (?, ?)",
            (user_id, file_id)
        )

        conn.commit()

    else:

        await message.reply_text(
            "👋 Welcome to Course Bot\n\nSend /watch to see your lectures."
        )
