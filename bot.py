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

        await query.message.reply_text(
            "💎 Premium Plan\n\n"
            "💰 ₹100 = 5 Bots\n\n"
            "📸 Send payment screenshot to admin.\n\n"
            "👨‍💻 Admin: @lokiiix46",
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
        if __name__ == "__main__":
    main()
