from pyrogram.types import Message
from utils.database import broadcast_all, set_user_limit, clear_user_uploads

async def broadcast_handler(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast.")
    count = await broadcast_all(client, message.reply_to_message)
    await message.reply_text(f"📢 Broadcast sent to {count} users.")

async def set_limit_handler(client, message: Message):
    try:
        user_id, limit = message.text.split()[1:]
        await set_limit(int(user_id), int(limit))
        await message.reply_text("✅ Limit set.")
    except:
        await message.reply_text("❌ Usage: /limit user_id limit")

async def clear_limit_handler(client, message: Message):
    await clear_all_limits()
    await message.reply_text("✅ All limits cleared.")
