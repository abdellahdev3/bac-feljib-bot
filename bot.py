import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update, ChatMember
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = "@bacfeljib"

async def is_subscribed(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in [
            ChatMember.MEMBER,
            ChatMember.ADMINISTRATOR,
            ChatMember.OWNER,
        ]
    except:
        return False

def get_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("〚 الدخول إلى المنصة 〛", web_app=WebAppInfo(url="https://bac-feljib.com"))],
        [InlineKeyboardButton("〚 كويزات البكالوريا 〛", web_app=WebAppInfo(url="https://quiz.bac-feljib.com"))],
        [InlineKeyboardButton("〚 حقيبة عقبة بن نافع 〛", web_app=WebAppInfo(url="https://okba.bac-feljib.com"))],
        [InlineKeyboardButton("〚 نجم البكالوريا 〛", web_app=WebAppInfo(url="https://star.bac-feljib.com"))],
        [
            InlineKeyboardButton("〚 ضفني لمجموعتك 〛", url="https://t.me/Bacfeljib_bot?startgroup=true"),
            InlineKeyboardButton("〚 شاركني لصديق 〛", url="https://t.me/share/url?url=https://t.me/Bacfeljib_bot"),
        ],
        [InlineKeyboardButton("〚 تابع قناتنا الرسمية 〛", url="https://t.me/bacfeljib")],
    ])

def get_subscribe_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 تابع القناة الرسمية", url="https://t.me/bacfeljib")],
        [InlineKeyboardButton("✅ تحققت، متابع", callback_data="check_sub")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not await is_subscribed(user_id, context):
        await update.message.reply_text(
            "⚠️ يجب متابعة قناتنا الرسمية أولاً للوصول إلى المنصة 👇",
            reply_markup=get_subscribe_keyboard()
        )
        return
    await update.message.reply_text(
        "☆ مرحبًا بك في Bac Feljib 🎓\n\nاختر ما تريد:",
        reply_markup=get_main_keyboard()
    )

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    if not await is_subscribed(user_id, context):
        await query.answer("❌ لم نتحقق من متابعتك، تأكد ثم حاول مجدداً", show_alert=True)
        return
    await query.message.edit_text(
        "☆ مرحبًا بك في Bac Feljib 🎓\n\nاختر ما تريد:",
        reply_markup=get_main_keyboard()
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_subscription, pattern="check_sub"))
    print("Bot is running...")
    app.run_polling()
