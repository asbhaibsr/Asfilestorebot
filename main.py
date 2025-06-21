from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from dotenv import load_dotenv
from handlers import start, help_cmd, genlink, multigenlink, mystats, stats, admin, utr
from utils.database import get_db
import os

# Load config.env file
load_dotenv("config.env")

# Bot credentials from .env
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ADMIN_ID = int(os.getenv("ADMIN"))

# Initialize bot
bot = Client("FileStoreBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
db = get_db()

# Add command handlers
bot.add_handler(MessageHandler(filters.command("start") & filters.private, start.start_cmd))
bot.add_handler(MessageHandler(filters.command("help") & filters.private, help_cmd.help_cmd))
bot.add_handler(MessageHandler(filters.command("genlink") & filters.private, genlink.genlink_handler))
bot.add_handler(MessageHandler(filters.command("multigenlink") & filters.private, multigenlink.multi_genlink_handler))
bot.add_handler(MessageHandler(filters.command("mystats") & filters.private, mystats.mystats_handler))
bot.add_handler(MessageHandler(filters.command("stats") & filters.private, stats.stats_handler))

# Admin-only commands
bot.add_handler(MessageHandler(filters.command("broadcast") & filters.user(ADMIN_ID), admin.broadcast_handler))
bot.add_handler(MessageHandler(filters.command("limit") & filters.user(ADMIN_ID), admin.set_limit_handler))
bot.add_handler(MessageHandler(filters.command("clearlimit") & filters.user(ADMIN_ID), admin.clear_limit_handler))
bot.add_handler(MessageHandler(filters.command("checkutr") & filters.user(ADMIN_ID), utr.check_utr_handler))

# UTR flow handlers
bot.add_handler(MessageHandler(filters.regex("Send UTR"), utr.utr_handler))
bot.add_handler(CallbackQueryHandler(utr.handle_callback_buttons))

print("🤖 Bot is running...")
bot.run()
