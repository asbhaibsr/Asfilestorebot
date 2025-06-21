from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import get_user_stats

async def stats_handler(client: Client, message: Message):
    user_id = message.from_user.id
    stats = await get_user_stats(user_id)

    await message.reply_text(
        f"📊 Your Plan Info:\n"
        f"📁 Uploads Used: {stats['used']}\n"
        f"📦 Total Limit: {stats['limit']}\n"
        f"💎 Premium: {'✅ Yes' if stats['is_premium'] else '❌ No'}\n"
        f"⏱️ File visibility: 5 minutes only after opening"
    )
