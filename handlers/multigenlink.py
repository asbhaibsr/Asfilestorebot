from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.database import save_multi_file, check_multi_limit

multi_uploads = {}

async def multi_genlink_handler(client: Client, message: Message):
    user_id = message.from_user.id

    if message.text and message.text.startswith("/multigenlink"):
        multi_uploads[user_id] = []
        await message.reply_text(
            "📥 Send up to 15 files one by one. When done, click the button below.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ Generate Link", callback_data="generate_multi")]])
        )
        return

    if message.document or message.video or message.audio:
        files = multi_uploads.get(user_id, [])
        if len(files) >= 15:
            return await message.reply_text("🚫 Limit reached! You can only upload 15 files. Buy premium for more.")

        link = await save_multi_file(message)
        multi_uploads[user_id].append(link)
        await message.reply_text(f"✅ File saved {len(files)+1}/15. Upload next or click Generate.")
