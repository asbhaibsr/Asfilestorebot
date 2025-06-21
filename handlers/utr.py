from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from utils.database import add_utr_request, get_pending_utrs, confirm_premium

pending_utrs = {}

async def utr_handler(client: Client, message: Message):
    user_id = message.from_user.id
    pending_utrs[user_id] = {"time": message.date}
    await message.reply_text("🕐 Send your UTR number now. You have 5 minutes.\n/cancel to stop.")

async def handle_callback_buttons(client: Client, query: CallbackQuery):
    data = query.data

    if data.startswith("buy_"):
        plan = data.split("_")[1]
        await query.message.edit(
            f"💳 UPI ID: <code>arsadsaifi8272@ibl</code>\n"
            f"🖼 QR: [Click to View]({os.getenv('QR_IMAGE')})\n\n"
            "✅ After payment, click the button below to send UTR number.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Send UTR", callback_data="sendutr")]])
        )

    elif data == "sendutr":
        await query.message.reply_text("Send your UTR number in the next 5 minutes...")

    elif data.startswith("approveutr_"):
        user_id = int(data.split("_")[1])
        await query.message.edit(
            "✅ Choose limit to assign:",
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
        await query.message.edit(f"✅ User {user_id} upgraded to Premium with limit: {limit}")

    elif data.startswith("rejectutr_"):
        await query.message.edit("❌ Rejected UTR request.")

async def check_utr_handler(client: Client, message: Message):
    utrs = await get_pending_utrs()
    if not utrs:
        return await message.reply_text("❌ No UTRs pending.")

    for user_id, info in utrs.items():
        await message.reply_text(
            f"👤 User: {user_id}\n💳 Plan: {info['plan']}\n\nApprove or Reject?",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ Add Premium", callback_data=f"approveutr_{user_id}")],
                [InlineKeyboardButton("❌ Reject", callback_data=f"rejectutr_{user_id}")]
            ])
        )
