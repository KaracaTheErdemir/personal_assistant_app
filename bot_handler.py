import requests
import asyncio
import executor as exc
import logging
from telegram import Bot, ForceReply, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    Application,
)

config = exc.get_telegram_config()
TELEGRAM_TOKEN = config['token']
CHAT_ID = config['chat_id']

# Define states for the ConversationHandler
FIRST, SECOND = range(2)

# Handler for the /start command
def start(update: Update, context):
    update.message.reply_text("Hello! This is your bot.")
    return FIRST

# Handler for the /cancel command
def cancel(update: Update, context):
    update.message.reply_text("Cancelled.")
    return ConversationHandler.END

# Handler for the first step in the conversation
def step_one(update: Update, context):
    update.message.reply_text("You are in step one. Please type something.")

    # Set the next step as SECOND
    return SECOND

# Handler for the second step in the conversation
def step_two(update: Update, context):
    user_input = update.message.text
    update.message.reply_text(f"You typed: {user_input}")

    return ConversationHandler.END  # End the conversation

async def handle_message(update: Update):
    await update.message.reply_text(f"yolo swag")


async def send_message():
    # Create a Bot instance
    bot = Bot(token=TELEGRAM_TOKEN)
    # Send a message
    await bot.send_message(chat_id=CHAT_ID, text='IM ALIVE')

async def start_bot():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers to the Application
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('cancel', cancel))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [MessageHandler(filters.TEXT, step_one)],
            SECOND: [MessageHandler(filters.TEXT, step_two)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    ))
    logging.info("Starthing the bot")
    await send_message()
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # Start the bot
    # await app.run_polling()

    # Run the bot until the user presses Ctrl-C
    # await app.idle()
