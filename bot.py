from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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
