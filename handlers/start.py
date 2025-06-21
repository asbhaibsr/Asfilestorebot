from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

WELCOME_TEXT = """
👋 Welcome to the File Store Bot!

📁 Upload any file to get a permanent download link.
🔗 Links are permanent, but files will be available for 5 minutes only.
💎 Free users can upload up to 500 files.
🔥 Upgrade to get more!
"""

START_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("📤 Upload File (/genlink)", callback_data="genlink")],
    [InlineKeyboardButton("📂 Multi Upload (/multigenlink)", callback_data="multigenlink")],
    [InlineKeyboardButton("💎 Buy Premium", callback_data="buy_premium")],
    [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
])

async def start_cmd(client: Client, message: Message):
    await message.reply_text(
        text=WELCOME_TEXT,
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )
