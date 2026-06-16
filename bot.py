from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import sqlite3
import os

TOKEN = os.getenv("TOKEN")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    plan TEXT DEFAULT 'free',
    bot_count INTEGER DEFAULT 0
)
""")
conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)",
        (user.id, user.username)
    )
    conn.commit()

    await update.message.reply_text(
        "🚀 Welcome to Master Bot Hosting!\n\n"
        "➕ Host Bot\n"
        "📂 My Bots\n"
        "💎 Premium\n"
        "👤 Account\n"
        "ℹ️ Help"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
