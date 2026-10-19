import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")

AUTO_REPLIES = {
    "salom": "Salom 😊",
    "assalomu alaykum": "Va alaykum assalom 😊",
    "qalaysan": "Yaxshi, rahmat 😊 O'zingizchi?",
    "qalesan": "Yaxshi 😄 O'zingiz qalaysiz?",
    "yaxshimisan": "Ha, rahmat 😊",
    "nima gap": "Tinchlik 😄 Sizda nima gap?",
    "nima qilyapsan": "Savollarga javob berib o'tiribman 😄",
    "kimsan": "Men savol-javob botiman 🤖",
    "isming nima": "Meni Orzu bot deb chaqirishingiz mumkin 😊",
    "necha yoshdasan": "Botlarda yosh bo'lmaydi-ku 😄",
    "rahmat": "Arzimaydi 🫶",
    "raxmat": "Arzimaydi 🫶",
    "xayr": "Xayr 👋 Yana yozing!",
    "hayr": "Xayr 👋",
    "yaxshi tun": "Yaxshi tun 🌙",
    "hayrli tong": "Hayrli tong ☀️",
    "zerikdim": "Unda menga biror qiziq savol bering 😄",
    "nima qila olasan": "Savollaringizni qabul qilaman va ayrimlariga o'zim javob beraman 🤖",
    "seni kim yaratgan": "Meni egam yaratgan 😄",
    "botmisan": "Ha, men Telegram botman 🤖",
    "sevgi nima": "Sevgi — juda katta mavzu 😄❤️"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom 👋\nMenga savolingizni yozing 😊\n\n"
        "Bot egasi uchun: /myid"
    )

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sizning Telegram ID raqamingiz: {update.effective_user.id}"
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    # ?, ! va . belgilarini hisobga olmaslik
    clean_text = text.rstrip("?!.")

    if clean_text in AUTO_REPLIES:
        await update.message.reply_text(AUTO_REPLIES[clean_text])
    else:
        await update.message.reply_text(
            "Savolingiz qabul qilindi 💌\n"
            "Bot egasi imkon topishi bilan javob beradi 😊"
        )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    app.run_polling()

if __name__ == "__main__":
    main()
