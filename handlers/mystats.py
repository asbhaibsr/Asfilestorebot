from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import get_user_stats

async def mystats_handler(client: Client, message: Message):
    user_id = message.from_user.id
    stats = await get_user_stats(user_id)

    await message.reply_text(
        f"👤 Your Stats:\n"
        f"🔢 Uploaded: {stats['used']}/{stats['limit']}\n"
        f"💎 Premium: {'✅ Yes' if stats['is_premium'] else '❌ No'}"
    )
