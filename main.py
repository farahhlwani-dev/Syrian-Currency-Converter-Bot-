from telegram.ext import ApplicationBuilder,CommandHandler,CallbackQueryHandler,MessageHandler,filters
from handlers.start import start,button_handler,message_handler
from dotenv import load_dotenv
import os

load_dotenv("token.env")
BOT_TOKEN=os.getenv("BOT_TOKEN")

def main():
    app=ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    app.run_polling()

if __name__ =="__main__":
    main()
