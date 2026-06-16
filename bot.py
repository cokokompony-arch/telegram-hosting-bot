import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8618104541:AAHTKfKEEcAzCvuAhg7b2l-pGshkkQrgOqA"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Bot Hosting Panel\n\n"
        "Upload:\n"
        "• bot.py\n"
        "• requirements.txt\n\n"
        "Commands:\n"
        "/mybots"
    )


async def upload_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document:
        return

    doc = update.message.document
    user_id = update.effective_user.id

    folder = f"user_bots/{user_id}"
    os.makedirs(folder, exist_ok=True)

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

    for f in files:
        text += f"• {f}\n"

    await update.message.reply_text(text)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("mybots", mybots)
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
