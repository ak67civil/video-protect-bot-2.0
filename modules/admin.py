from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        "Welcome to Course Bot 🎓\n\nYour access will be verified."
    )
