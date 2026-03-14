 from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(client, message):

    await message.reply_text(
        "📚 Welcome to Course Bot\n\n"
        "Click lectures from index channel to watch."
    )
