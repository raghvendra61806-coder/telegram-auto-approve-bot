from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request

    await context.bot.approve_chat_join_request(
        chat_id=req.chat.id,
        user_id=req.from_user.id
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(ChatJoinRequestHandler(approve))

print("Bot Started...")
app.run_polling()
