from pyrogram.types import Message
from utils.database import get_user_stats

async def mystats_handler(client, message: Message):
    stats = await get_user_stats(message.from_user.id)
    await message.reply_text(f"📊 Your Stats:\nFiles Uploaded: {stats['files']}\nLimit: {stats['limit']}")
