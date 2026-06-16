import os
import sqlite3

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8618104541:AAHTKfKEEcAzCvuAhg7b2l-pGshkkQrgOqA"
ADMIN_ID = 8809781461

# Database
db = sqlite3.connect("database.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    plan TEXT DEFAULT 'free'
)
""")

db.commit()


def add_user(user_id):
    cur.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    db.commit()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)

    keyboard = [
        [InlineKeyboardButton("➕ Host Bot", callback_data="host")],
        [InlineKeyboardButton("📂 My Bots", callback_data="mybots")],
        [InlineKeyboardButton("▶️ Start Bot", callback_data="startbot")],
        [InlineKeyboardButton("⏹️ Stop Bot", callback_data="stopbot")],
        [InlineKeyboardButton("💎 Premium", callback_data="premium")],
        [InlineKeyboardButton("👤 Account", callback_data="account")]
    ]

    await update.message.reply_text(
        "🚀 Welcome To Bot Hosting Panel",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def upload_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document:
        return

    user_id = update.effective_user.id
    folder = f"user_bots/{user_id}"

    os.makedirs(folder, exist_ok=True)

    doc = update.message.document

    file = await doc.get_file()

    await file.download_to_drive(
        os.path.join(folder, doc.file_name)
    )

    await update.message.reply_text(
        f"✅ Saved: {doc.file_name}"
    )


async def mybots(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    folder = f"user_bots/{user_id}"

    if not os.path.exists(folder):
        await update.message.reply_text(
            "📂 No files uploaded."
        )
        return

    files = os.listdir(folder)

    if not files:
        await update.message.reply_text(
            "📂 No files uploaded."
        )
        return

    text = "📂 Your Files:\n\n"

    for file in files:
        text += f"• {file}\n"

    await update.message.reply_text(text)


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    await update.message.reply_text(
        f"👑 Admin Panel\n\n"
        f"👤 Users: {users}"
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == "host":
        await query.message.reply_text(
            "📤 Send bot.py and requirements.txt"
        )

    elif query.data == "mybots":
        folder = f"user_bots/{user_id}"

        if not os.path.exists(folder):
            await query.message.reply_text(
                "📂 No bots uploaded."
            )
            return

        files = "\n".join(os.listdir(folder))

        await query.message.reply_text(
            f"📂 Your Files:\n\n{files}"
        )

    elif query.data == "startbot":
        await query.message.reply_text(
            "▶️ Start Bot feature coming soon"
        )

    elif query.data == "stopbot":
        await query.message.reply_text(
            "⏹️ Stop Bot feature coming soon"
        )

    elif query.data == "premium":
    keyboard = [
        [
            InlineKeyboardButton(
                "📞 Contact Admin",
                url="https://t.me/lokiiix46"
            )
        ]
    ]

    await query.message.reply_photo(
        photo="https://i.ibb.co/SXNn3wzZ/payment.jpg",
        caption=(
            "💎 PREMIUM PLAN 💎\n\n"
            "💰 Price: ₹100\n"
            "🤖 Premium Limit: 5 Bots\n\n"
            "📸 After payment, send the payment screenshot to the admin.\n"
            "✅ Your premium plan will be activated after verification.\n\n"
            "👨‍💻 Admin: @lokiiix46"
        ),
        reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "account":
    cur.execute(
        "SELECT plan FROM users WHERE user_id=?",
        (user_id,)
    )

    row = cur.fetchone()
    plan = row[0] if row else "free"

    await query.message.reply_text(
        f"👤 Account\n\n"
        f"🆔 {user_id}\n"
        f"💎 Plan: {plan}"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("mybots", mybots)
    )

    app.add_handler(
        CommandHandler("admin", admin)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    app.add_handler(
        MessageHandler(
            filters.Document.ALL,
            upload_file
        )
    )

    print("Hosting Panel Started")

    app.run_polling()


if __name__ == "__main__":
    main()
