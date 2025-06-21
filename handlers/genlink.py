from pyrogram import Client, filters
from pyrogram.types import Message
from utils.database import save_file, user_limit_ok

async def genlink_handler(client: Client, message: Message):
    if not message.document and not message.video and not message.audio:
        return await message.reply_text("❗ Send a file to generate a link.")

    user_id = message.from_user.id
    if not await user_limit_ok(user_id):
        return await message.reply_text("🚫 You've reached your upload limit. Buy premium to continue.")

    link = await save_file(message)
    await message.reply_text(f"✅ File saved!\n📎 Link: {link}\n⏱️ File visible for 5 minutes after open.")
