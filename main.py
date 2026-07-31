import os
import random
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "7344229701"))

def load_roasts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return ["Roast list khali hai bhai"]

roasts = {
    'hs': load_roasts('roasts/hs.txt'),
    'es': load_roasts('roasts/es.txt'),
    'hr': load_roasts('roasts/hr.txt'),
    'er': load_roasts('roasts/er.txt')
    'hi': load_roasts('roasts/hi.txt')
    'he': load_roasts('roasts/he.txt')
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Ultimate Roaster ON! 🔥\n\n/hindi - Hindi roast\n/english - English roast\n/hinglish - Hinglish roast\n/english_hindi - English+Hindi roast")

async def roast_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, lang):
    roast = random.choice(roasts.get(lang, ["Kuch nahi mila"]))
    await update.message.reply_text(f"🔥 {roast}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hindi", lambda u,c: roast_cmd(u,c,'hs')))
    app.add_handler(CommandHandler("english", lambda u,c: roast_cmd(u,c,'es')))
    app.add_handler(CommandHandler("hinglish", lambda u,c: roast_cmd(u,c,'hr')))
    app.add_handler(CommandHandler("english_hindi", lambda u,c: roast_cmd(u,c,'er')))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
