from pyrogram.types import Message
from utils.database import get_bot_stats

async def stats_handler(client, message: Message):
    stats = await get_bot_stats()
    await message.reply_text(f"📈 Bot Stats:\nTotal Users: {stats['users']}\nTotal Files: {stats['files']}")
