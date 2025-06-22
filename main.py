# ✅ Fully Fixed & Simplified `main.py` for Asfilestorebot

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from dotenv import load_dotenv
import os

from handlers import start, help_cmd, genlink, multigenlink, mystats, stats, admin, utr
from utils.database import get_db

load_dotenv("config.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ADMIN_ID = int(os.getenv("ADMIN"))

bot = Client("FileStoreBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = get_db()

@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await start.start_cmd(client, message)

@bot.on_message(filters.command("help") & filters.private)
async def help_handler(client, message: Message):
    await help_cmd.help_cmd(client, message)

@bot.on_message(filters.command("genlink") & filters.private)
async def genlink_handler(client, message: Message):
    await genlink.genlink_handler(client, message)

@bot.on_message(filters.command("multigenlink") & filters.private)
async def multigenlink_handler(client, message: Message):
    await multigenlink.multi_genlink_handler(client, message)

@bot.on_message(filters.command("mystats") & filters.private)
async def mystats_handler(client, message: Message):
    await mystats.mystats_handler(client, message)

@bot.on_message(filters.command("stats") & filters.private)
async def stats_handler(client, message: Message):
    await stats.stats_handler(client, message)

@bot.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast_handler(client, message: Message):
    await admin.broadcast_handler(client, message)

@bot.on_message(filters.command("limit") & filters.user(ADMIN_ID))
async def limit_handler(client, message: Message):
    await admin.set_limit_handler(client, message)

@bot.on_message(filters.command("clearlimit") & filters.user(ADMIN_ID))
async def clearlimit_handler(client, message: Message):
    await admin.clear_limit_handler(client, message)

@bot.on_message(filters.command("checkutr") & filters.user(ADMIN_ID))
async def checkutr_handler(client, message: Message):
    await utr.check_utr_handler(client, message)

@bot.on_message(filters.regex("Send UTR") & filters.private)
async def handle_utr(client, message: Message):
    await utr.utr_handler(client, message)

@bot.on_callback_query()
async def callback_query_handler(client, callback_query: CallbackQuery):
    await utr.handle_callback_buttons(client, callback_query)

print("\n✅ FileStoreBot is running...")
bot.run()
