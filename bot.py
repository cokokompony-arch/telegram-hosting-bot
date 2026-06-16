from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "TOKEN"
CHANNEL_ID = -1003957806196

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!\n\nSend me a photo or video and I will save it."
    )

async def save_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    await context.bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=photo.file_id,
        caption=f"Saved from {update.effective_user.id}"
    )
    await update.message.reply_text("✅ Photo saved.")

async def save_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    await context.bot.send_video(
        chat_id=CHANNEL_ID,
        video=video.file_id,
        caption=f"Saved from {update.effective_user.id}"
    )
    await update.message.reply_text("✅ Video saved.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, save_photo))
    app.add_handler(MessageHandler(filters.VIDEO, save_video))

    app.run_polling()

if __name__ == "__main__":
    main()
