from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import broadcast_all, set_user_limit, clear_user_uploads

async def broadcast_handler(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("❗ Reply to a message to broadcast.")
    await broadcast_all(message.reply_to_message)
    await message.reply_text("✅ Broadcast started.")

async def set_limit_handler(client: Client, message: Message):
    try:
        user_id, limit = message.text.split()[1:3]
        await set_user_limit(int(user_id), int(limit))
        await message.reply_text("✅ Limit updated.")
    except:
        await message.reply_text("❗ Usage: /limit user_id number")

async def clear_limit_handler(client: Client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        await clear_user_uploads(user_id)
        await message.reply_text("✅ User upload count reset.")
    except:
        await message.reply_text("❗ Usage: /clearlimit user_id")
