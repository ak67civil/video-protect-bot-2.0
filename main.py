@bot.on_message(filters.chat(UPLOAD_CHANNEL) & filters.video)
async def upload_video(client, message):

    caption = message.caption if message.caption else "🎬 New Video"

    try:
        sent = await client.send_video(
            chat_id=INDEX_CHANNEL,
            video=message.video.file_id,
            caption=caption,
            protect_content=True
        )
    except Exception as e:
        print("VIDEO SEND ERROR:", e)

    await client.forward_messages(
        chat_id=LOG_CHANNEL,
        from_chat_id=UPLOAD_CHANNEL,
        message_ids=[message.id]
    )

    print("✅ Video Indexed")
