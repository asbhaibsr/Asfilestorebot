from pyrogram.types import Message, CallbackQuery
from utils.database import save_utr, approve_utr, reject_utr

async def check_utr_handler(client, message: Message):
    # Dummy for now
    await message.reply_text("🧾 No UTRs pending.")

async def utr_handler(client, message: Message):
    await save_utr(message.from_user.id, message.text)
    await message.reply_text("✅ UTR submitted. We'll verify soon.")

async def handle_callback_buttons(client, callback_query: CallbackQuery):
    data = callback_query.data

    if data == "genlink":
        await callback_query.message.reply("/genlink likho ya file bhejo")
    elif data == "multigen":
        await callback_query.message.reply("/multigenlink likho")
    elif data == "plans":
        await callback_query.message.reply("💎 VIP Plans:\n₹30 = 30 files\n₹60 = 80 files")
    elif data == "help":
        await callback_query.message.reply("/help likho full command list ke liye")
    elif data == "generate_multi":
        # You can update logic here if needed
        await callback_query.message.reply("🔗 Link generated for multi-files.")
    else:
        await callback_query.message.reply("❓ Unknown button.")
