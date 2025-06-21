from pyrogram import Client, filters
from pyrogram.types import Message

HELP_TEXT = """
ℹ️ <b>How to use this bot:</b>

✅ Use /genlink to upload a single file and get a link
✅ Use /multigenlink to upload 15 files one by one and get 1 combined link
✅ You can upload up to 500 files for FREE

💎 To increase your limit:
- ₹100 = 1000 uploads
- ₹300 = 3000 uploads
- ₹500 = 5000 uploads
- ₹1000 = Permanent (10,000 uploads)

⏱️ Files will auto-delete after 5 minutes once opened
🔗 But links are permanent

💬 Use /mystats to check your plan & usage
"""

async def help_cmd(client: Client, message: Message):
    await message.reply_text(HELP_TEXT, disable_web_page_preview=True)
