from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.database import save_multi_file, check_multi_limit

multi_uploads = {}

# /multigenlink command handler
async def multi_genlink_handler(client: Client, message: Message):
    user_id = message.from_user.id

    if message.text and message.text.startswith("/multigenlink"):
        multi_uploads[user_id] = []
        await message.reply_text(
            "📥 Send up to 15 files one by one.\nWhen done, tap the button below.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Generate Link", callback_data="generate_multi")]
            ])
        )
        return

    # Handle each file upload
    if message.document or message.video or message.audio:
        files = multi_uploads.get(user_id, [])
        if len(files) >= 15:
            return await message.reply_text("🚫 Limit reached! You can only upload 15 files.\nUpgrade to premium for more.")

        link = await save_multi_file(message)
        multi_uploads[user_id].append(link)
        await message.reply_text(f"✅ File saved {len(files)+1}/15. Upload next or click Generate.")

# ✅ Callback handler for Generate Link button
@Client.on_callback_query(filters.regex("generate_multi"))
async def generate_multi_link(client: Client, callback: CallbackQuery):
    user_id = callback.from_user.id
    links = multi_uploads.get(user_id)

    if not links:
        return await callback.message.reply_text("❌ No files uploaded yet.")

    text = "🔗 Your file links:\n\n" + "\n".join(links)
    await callback.message.reply_text(text)
    multi_uploads.pop(user_id, None)  # Clear after use
