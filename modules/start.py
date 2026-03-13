from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):

    if len(message.command) > 1:
        file_id = message.command[1]

        await message.reply_video(
            file_id,
            caption="🎬 Enjoy your lecture"
        )

    else:
        await message.reply_text(
            "Welcome to Course Bot 🎓"
        )
