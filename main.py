import os
import random
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "7344")) # default id change kar lena

def load_roasts(file_path):
    """txt file se saare roasts load karega"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return ["Roast list khali hai bhai 😭 file nahi mili"]
    except Exception as e:
        logging.error(f"Error loading {file_path}: {e}")
        return ["Roast load karte time error aa gayi"]

# Saare roast styles load karna
roastimport os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_roasts(file_name):
    """txt file se saare roasts load karega"""
    file_path = os.path.join(BASE_DIR, "roasts", file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = [line.strip() for line in f if line.strip()]
            if not data:
                return ["Is style me roast nahi hai 😅 file khali hai"]
            return data
    except FileNotFoundError:
        return [f"Roast list khali hai bhai file nahi mili: {file_path}"]
    except Exception as e:
        return [f"Error: {e}"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Roast Bot On hai!\n\n"
        "Commands:\n"
        "/roast hs - Hindi Savage\n"
        "/roast es - English Savage\n"
        "/roast hr - Hindi Rizz\n"
        "/roast er - English Rizz\n"
        "/roast hi - Hindi Insult\n"
        "/roast he - Hinglish\n"
        "/styles - Saare styles dekhne ke liye"
    )

async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Style batao bhai! /roast es ya /roast hs")
        return

    style = context.args[0].lower()

    if style not in roasts:
        await update.message.reply_text(f"Style nahi mila. /styles se list check kar lo")
        return

    roast_list = roasts[style]
    if not roast_list:
        await update.message.reply_text("Is style me roast nahi hai 😅")
        return

    selected_roast = random.choice(roast_list)
    await update.message.reply_text(f"🔥 {selected_roast}")

async def styles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    style_names = {
        'hs': 'Hindi Savage',
        'es': 'English Savage',
        'hr': 'Hindi Rizz',
        'er': 'English Rizz',
        'hi': 'Hindi Insult',
        'he': 'Hinglish Mix'
    }
    msg = "Available Roast Styles:\n\n"
    for key, name in style_names.items():
        count = len(roasts.get(key, []))
        msg += f"/roast {key} - {name} [{count} roasts]\n"
    await update.message.reply_text(msg)

def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN env me set karo!")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roast", roast))
    app.add_handler(CommandHandler("styles", styles))

    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
