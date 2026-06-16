from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import os

TOKEN = "8618104541:AAHTKfKEEcAzCvuAhg7b2l-pGshkkQrgOqA"

# STEP 2 FUNCTION
async def upload_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document

    if not doc:
        return

    user_id = update.effective_user.id
    folder = f"user_bots/{user_id}"
    os.makedirs(folder, exist_ok=True)

    file = await doc.get_file()
    await file.download_to_drive(f"{folder}/{doc.file_name}")

    await update.message.reply_text(f"✅ Saved {doc.file_name}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send bot.py and requirements.txt"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

# STEP 2 HANDLER
app.add_handler(
    MessageHandler(filters.Document.ALL, upload_file)
)

app.run_polling()
