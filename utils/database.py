import motor.motor_asyncio
import os, random
from dotenv import load_dotenv
import ast

load_dotenv("config.env")

def get_db():
    mongo_list = ast.literal_eval(os.getenv("MONGO_URIS"))
    for entry in mongo_list:
        if entry["active"]:
            return motor.motor_asyncio.AsyncIOMotorClient(entry["uri"]).filestore
    return None

db = get_db()

# Get user stats like used files, limit and premium status
async def get_user_stats(user_id):
    user = await db.users.find_one({"_id": user_id}) or {}
    return {
        "used": user.get("count", 0),
        "limit": user.get("limit", int(os.getenv("DEFAULT_LIMIT"))),
        "is_premium": user.get("premium", False)
    }

# Check if user is within their upload limit
async def user_limit_ok(user_id):
    user = await db.users.find_one({"_id": user_id}) or {}
    return user.get("count", 0) < user.get("limit", int(os.getenv("DEFAULT_LIMIT")))

# Save a single file
async def save_file(message):
    user_id = message.from_user.id
    await db.users.update_one({"_id": user_id}, {"$inc": {"count": 1}}, upsert=True)
    return f"https://t.me/{os.getenv('CHANNEL_USERNAME').strip('@')}/{random.randint(1000,9999)}"

# Save file used in multigenlink
async def save_multi_file(message):
    return await save_file(message)

# Broadcast to all users
async def broadcast_all(msg):
    async for user in db.users.find():
        try:
            await msg.copy(user["_id"])
        except:
            pass

# Admin sets custom upload limit
async def set_user_limit(user_id, new_limit):
    await db.users.update_one({"_id": user_id}, {"$set": {"limit": new_limit}}, upsert=True)

# Clear user upload count
async def clear_user_uploads(user_id):
    await db.users.update_one({"_id": user_id}, {"$set": {"count": 0}}, upsert=True)

# UTR Section (payment tracking)
utr_store = {}

async def add_utr_request(user_id, plan):
    utr_store[user_id] = {"plan": plan}

async def get_pending_utrs():
    return utr_store

async def confirm_premium(user_id, limit):
    await set_user_limit(user_id, limit)
    await db.users.update_one({"_id": user_id}, {"$set": {"premium": True}}, upsert=True)
    if user_id in utr_store:
        del utr_store[user_id]

# ✅ Missing function that caused error in multigenlink.py
async def check_multi_limit(user_id):
    user = await db.users.find_one({"_id": user_id}) or {}
    return user.get("multi_upload_count", 0)
