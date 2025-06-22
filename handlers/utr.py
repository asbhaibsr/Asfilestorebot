from pyrogram import Client
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.database import add_utr_request, get_pending_utrs, confirm_premium
import os

pending_utrs = {}

async def utr_handler(client: Client, message: Message):
    user_id = message.from_user.id
    pending_utrs[user_id] = {"time": message.date}
    await message.reply_text("🕐 Apna UTR number bheje. Aapke paas 5 minute hai.\n/cancel likh kar band kare.")

async def handle_callback_buttons(client: Client, query: CallbackQuery):
    data = query.data

    if data.startswith("buy_"):
        plan = data.split("_")[1]
        await add_utr_request(query.from_user.id, plan)
        await query.message.edit(
            f"💳 UPI ID: <code>arsadsaifi8272@ibl</code>\n"
            f"🖼 QR: [Click to View]({os.getenv('QR_IMAGE')})\n\n"
            "✅ Payment ke baad niche wale button se UTR bheje:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📝 Send UTR", callback_data="sendutr")],
                [InlineKeyboardButton("❌ Cancel", callback_data="cancelutr")]
            ])
        )

    elif data == "sendutr":
        await query.message.reply_text("Apna UTR number bheje. 5 minute ke andar.")

    elif data == "cancelutr":
        await query.message.edit("❌ UTR process cancel kar diya gaya.")

    elif data.startswith("approveutr_"):
        user_id = int(data.split("_")[1])
        await query.message.edit(
            "✅ Kitna limit dena chahte ho?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("500", callback_data=f"give_500_{user_id}")],
                [InlineKeyboardButton("1000", callback_data=f"give_1000_{user_id}")],
                [InlineKeyboardButton("3000", callback_data=f"give_3000_{user_id}")],
                [InlineKeyboardButton("5000", callback_data=f"give_5000_{user_id}")],
                [InlineKeyboardButton("Unlimited (10000)", callback_data=f"give_unlimited_{user_id}")]
            ])
        )

    elif data.startswith("give_"):
        parts = data.split("_")
        limit = 10000 if parts[1] == "unlimited" else int(parts[1])
        user_id = int(parts[2])
        await confirm_premium(user_id, limit)
        await query.message.edit(f"✅ User {user_id} ko Premium banaya gaya. Limit: {limit}")

    elif data.startswith("rejectutr_"):
        await query.message.edit("❌ UTR request reject kiya gaya.")

async def check_utr_handler(client: Client, message: Message):
    utrs = await get_pending_utrs()
    if not utrs:
        return await message.reply_text("❌ Koi pending UTR nahi mila.")

    for user_id, info in utrs.items():
        await message.reply_text(
            f"👤 User: {user_id}\n💳 Plan: {info['plan']}\n\nApprove ya Reject karo:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Add Premium", callback_data=f"approveutr_{user_id}")],
                [InlineKeyboardButton("❌ Reject", callback_data=f"rejectutr_{user_id}")]
            ])
        )
