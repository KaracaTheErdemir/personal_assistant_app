import sys
import os
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
sys.path.append(os.path.abspath('/Users/hermestrismegistus/personal_assistant_app'))
from config_manager import get_telegram_config
from handlers.command_handler import list_entries, new_entry, report_entries, track_entry

config = get_telegram_config()
TELEGRAM_TOKEN = config['token']
CHAT_ID = config['chat_id']

# Handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! This is your bot.")
    context.user_data['started'] = True

# Handler for the /cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled.")
    context.user_data['started'] = False

async def send_message(message):
    # Create a Bot instance
    bot = Bot(token=TELEGRAM_TOKEN)
    # Send a message
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('started'):
        user_input = update.message.text
        message = f"did you just say {user_input}?"
        #mes = meeting_entry(user_input)
        #await update.message.reply_text(f"{mes}")
        
        await send_message(message)
    else:
        await update.message.reply_text("Please use /start to begin.")

async def start_bot():
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logging.getLogger('httpx').setLevel(logging.WARNING) # To avoid the flood of httpx info messages.

        app = Application.builder().token(TELEGRAM_TOKEN).build()
        # Add handlers to the Application
        app.add_handler(CommandHandler('cancel', cancel))
        app.add_handler(CommandHandler('start', start))
        #TODO: change this to reading command lines instead
        app.add_handler(MessageHandler(filters.Text(), handle_message))
        logging.info("Starting the bot")

        await app.initialize()
        await app.start()
        await app.updater.start_polling()
    except Exception as e:
            logging.error(f"An error occurred in start_bot: {type(e).__name__} - {str(e)}")

from telegram.ext import CommandHandler

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract the command and its arguments


    # Based on the command, call the appropriate function
    try:
        # Split the message into command and option
        parts = update.message.text.split()
        
        if len(parts) < 2 or not parts[1].startswith('-'):
            return "Invalid command format. Use an option starting with '-' after the command."
        
        command = parts[0]
        option = parts[1]

        # Route the command and option to the appropriate function
        if command == '/new':
            return new_entry(option)
        elif command == '/track':
            return track_entry(option)
        elif command == '/list':
            return list_entries(option)
        elif command == '/report':
            return report_entries(option)
        else:
            return "Unknown command."
    except Exception as e:
        logging.error(f"Error handling command: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing the command."

    
    # Send the response back to the user
    await update.message.reply_text(response)
