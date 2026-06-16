# Add near top of file
PAYMENT_IMAGE = None

# Add imports
from telegram.ext import ConversationHandler

WAITING_PAYMENT_IMAGE = 1


async def payment(update, context):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "📤 Send the payment QR image."
    )

    return WAITING_PAYMENT_IMAGE


async def save_payment_image(update, context):
    global PAYMENT_IMAGE

    PAYMENT_IMAGE = update.message.photo[-1].file_id

    await update.message.reply_text(
        "✅ Payment image saved successfully."
    )

    return ConversationHandler.END


async def cancel(update, context):
    return ConversationHandler.END
