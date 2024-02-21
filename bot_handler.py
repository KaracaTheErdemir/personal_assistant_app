import requests
import asyncio
import executor as exc
from telegram import Bot, ForceReply, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

config = exc.get_telegram_config()
TELEGRAM_TOKEN = config['token']
CHAT_ID = config['chat_id']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print("hi")
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
                                    
async def handle_message(update, context):
    message_text = update.message.text
    chat_id = update.message.chat_id
    print(f"Received message from chat ID {chat_id}: {message_text}")
    # Handle the received message here (store in database, perform some action, etc.)
    update.message.reply_text(f'Received message: {message_text}')

async def send_message():
    # Create a Bot instance
    bot = Bot(token=TELEGRAM_TOKEN)

    # Send a message
    await bot.send_message(chat_id=CHAT_ID, text='IM ALIVE BITCH')

async def start_bot():
    updater = Updater(TELEGRAM_TOKEN, update_queue=asyncio.Queue)
    await send_message()    
    #await handle_message(Update, context=any)
    # Run the bot until the user presses Ctrl-C
