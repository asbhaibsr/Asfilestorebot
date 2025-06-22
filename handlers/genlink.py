from pyrogram.types import Message
from utils.database import save_file

async def genlink_handler(client, message: Message):
    if message.document or message.video or message.audio:
        link = await save_file(message)
        await message.reply_text(f"✅ Link generated:\n{link}")
    else:
        await message.reply_text("❗Please send a file (video, doc, audio) to generate link.")
