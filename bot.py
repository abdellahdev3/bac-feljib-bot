import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("8711638250:AAEfUOOtoWgJbWlBRvj3d19wXYr27MSGjVs")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("〚 الدخول إلى المنصة 〛", web_app=WebAppInfo(url="https://bac-feljib.com"))],
        [InlineKeyboardButton("〚 كويزات البكالوريا 〛", web_app=WebAppInfo(url="https://quiz.bac-feljib.com"))],
        [InlineKeyboardButton("〚 حقيبة عقبة بن نافع 〛", web_app=WebAppInfo(url="https://okba.bac-feljib.com"))],
        [InlineKeyboardButton("〚 نجم البكالوريا 〛", web_app=WebAppInfo(url="https://star.bac-feljib.com"))],
        [
            InlineKeyboardButton("〚 ضفني لمجموعتك 〛", url="https://t.me/Bacfeljib_bot?startgroup=true"),
            InlineKeyboardButton("〚 شاركني لصديق 〛", url="https://t.me/share/url?url=https://t.me/Bacfeljib_bot"),
        ],
        [InlineKeyboardButton("〚 تابع قناتنا الرسمية 〛", url="https://t.me/bacfeljib")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "☆ مرحبًا بك في Bac Feljib 🎓\n\nاختر ما تريد:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()