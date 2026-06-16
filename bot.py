from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import sqlite3

TOKEN = os.getenv("TOKEN")

# Database
conn = sqlite3.connect("users.db", check_same_thread=False)
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
        f"👋 Welcome {user.first_name}!\n\n"
        f"🆔 User ID: {user.id}\n"
        f"📦 Plan: Free\n\n"
        f"⚠️ Free users can run bots for 24 hours.\n"
        f"💎 Premium Plan (3 Months): ₹100\n"
        f"📞 Contact: @lokiiix46"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Running...")
app.run_polling()
