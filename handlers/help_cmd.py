from pyrogram.types import Message

async def help_cmd(client, message: Message):
    await message.reply_text(
        "**📚 Help Menu:**\n\n"
        "/genlink - Generate short link for one file\n"
        "/multigenlink - Upload up to 15 files and generate links\n"
        "/mystats - View your usage stats\n"
        "/stats - View bot-wide stats\n"
        "/broadcast - (admin only)\n"
        "/limit - Set user limit (admin)\n"
        "/clearlimit - Clear limits (admin)\n"
        "/checkutr - Check UTRs (admin)\n"
    )
