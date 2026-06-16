from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8618104541:AAHTKfKEEcAzCvuAhg7b2l-pGshkkQrgOqA"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Premium", callback_data="premium")],
        [InlineKeyboardButton("👤 Account", callback_data="account")]
    ]

    await update.message.reply_text(
        "🚀 Welcome To Bot Hosting Panel",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if query.data == "premium":
        keyboard = [
            [
                InlineKeyboardButton(
                    "📞 Contact Admin",
                    url="https://t.me/lokiiix46"
                )
            ]
        ]

        await query.message.reply_text(
            "💎 PREMIUM PLAN 💎\n\n"
            "💰 ₹100 = 5 Bots\n\n"
            "📸 After payment send screenshot to admin.\n\n"
            "👨‍💻 Admin: @lokiiix46",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "account":
        await query.message.reply_text(
            f"👤 Account\n\n🆔 {user_id}"
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot Started")
    app.run_polling()


if __name__ == "__main__":
    main()
