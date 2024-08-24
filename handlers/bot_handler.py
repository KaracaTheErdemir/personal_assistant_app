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
from executor import get_telegram_config
from handlers.command_handler import list_expenses, list_friends, list_habits, list_meetings, new_expense, new_friend, new_meeting, track_habit

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
    command = update.message.text.split()[0]  # The command itself (e.g., /start)
    arguments = update.message.text.split()[1:]  # The arguments after the command

    # Based on the command, call the appropriate function
    if command == '/track':
        if len(arguments) > 0 and arguments[0] == 'habit':
            response = track_habit(' '.join(arguments[1:]))
        elif len(arguments) > 0 and arguments[0] == 'list':
            response = list_habits(' '.join(arguments[1:]))
        else:
            response = "Invalid subcommand for /track."
    
    elif command == '/meeting':
        if len(arguments) > 0 and arguments[0] == 'new':
            response = new_meeting(' '.join(arguments[1:]))
        elif len(arguments) > 0 and arguments[0] == 'list':
            response = list_meetings(' '.join(arguments[1:]))
        else:
            response = "Invalid subcommand for /meeting."
    
    elif command == '/objective':
        if len(arguments) > 0 and arguments[0] == 'set':
            response = set_objective(' '.join(arguments[1:]))
        elif len(arguments) > 0 and arguments[0] == 'list':
            response = list_objectives(' '.join(arguments[1:]))
        else:
            response = "Invalid subcommand for /objective."
    
    elif command == '/friend':
        if len(arguments) > 0 and arguments[0] == 'new':
            response = new_friend(' '.join(arguments[1:]))
        elif len(arguments) > 0 and arguments[0] == 'list':
            response = list_friends(' '.join(arguments[1:]))
        else:
            response = "Invalid subcommand for /friend."
    
    elif command == '/expense':
        if len(arguments) > 0 and arguments[0] == 'new':
            response = new_expense(' '.join(arguments[1:]))
        elif len(arguments) > 0 and arguments[0] == 'list':
            response = list_expenses(' '.join(arguments[1:]))
        else:
            response = "Invalid subcommand for /expense."
    
    else:
        response = "Unknown command."
    
    # Send the response back to the user
    await update.message.reply_text(response)
