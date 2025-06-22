from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def start_cmd(client, message: Message):
    buttons = [
        [InlineKeyboardButton("📥 Generate Link", callback_data="genlink")],
        [InlineKeyboardButton("📤 Multi Link", callback_data="multigen")],
        [InlineKeyboardButton("💎 Premium Plans", callback_data="plans")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
    ]
    await message.reply_text(
        f"👋 Hey {message.from_user.first_name}!\n\nWelcome to the VIP File Bot.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
