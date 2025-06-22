from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def start_cmd(client, message: Message):
    text = "Welcome to FileStore Bot."
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Buy Premium", callback_data="buy")],
    ])
    await message.reply_text(text, reply_markup=buttons)
