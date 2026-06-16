from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("➕ Host Bot", callback_data="host")],
        [InlineKeyboardButton("📂 My Bots", callback_data="mybots")],
        [InlineKeyboardButton("💎 Premium", callback_data="premium")],
        [InlineKeyboardButton("👤 Account", callback_data="account")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome Michael 🚀",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
