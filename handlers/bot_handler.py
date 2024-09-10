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
#sys.path.append(os.path.abspath('/Users/hermestrismegistus/personal_assistant_app'))
from config_manager import get_telegram_config
from handlers.command_handler import list_expenses, list_friends, list_habits, list_meetings, list_todos, new_expense, new_friend, new_habit, new_meeting, new_todo, track_habit, track_todo, update_expense, update_friend, update_habit, update_meeting, update_todo

config = get_telegram_config()
TELEGRAM_TOKEN = config['token']
CHAT_ID = config['chat_id']

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
        app.add_handler(MessageHandler(filters.Command, handle_command))
        #TODO: change this to reading command lines instead
        #app.add_handler(MessageHandler(filters.Text(), handle_message))
        logging.info("Starting the bot")

        await app.initialize()
        await app.start()
        await app.updater.start_polling()
    except Exception as e:
            logging.error(f"An error occurred in start_bot: {type(e).__name__} - {str(e)}")

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract the command and its arguments


    # Based on the command, call the appropriate function
    try:
        # Split the message into command and option
        parts = update.message.text.split()
        
        if len(parts) < 2:
            return "Invalid command format. Use an option starting with '-' after the command."
        
        command = parts[0]
        option = parts[1]
        payload = parts
        # Route the command and option to the appropriate function

        if command == '/new':
            if option == 'friend':
                return new_friend(parts)
            elif option == 'meeting':
                return new_meeting(parts)
            elif option == 'expense':
                return new_expense(parts)
            elif option == 'habit':
                return new_habit(parts)
            elif option == 'plan':
                return new_todo(parts)
            else:
                return "Invalid option for /new."

        elif command == '/update':
            if option == 'friend':
                return update_friend(parts)
            elif option == 'meeting':
                return update_meeting(parts)
            elif option == 'expense':
                return update_expense(parts)
            elif option == 'habit':
                return update_habit(parts)
            elif option == 'todo':
                return update_todo(parts)
            else:
                return "Invalid option for /update."

        elif command == '/track':
            if option == 'habit':
                return track_habit(parts)
            elif option == 'plan':
                return track_todo(parts)
            else:
                return "Invalid option for /track."

        elif command == '/list':
            if option == 'friends':
                return list_friends(parts)
            elif option == 'meetings':
                return list_meetings(parts)
            elif option == 'habits':
                return list_habits(parts)
            elif option == 'plans':
                return list_todos(parts)
            elif option == 'expenses':
                return list_expenses(parts)
            else:
                return "Invalid option for /list."


        else:
            return "Unknown command."
    except Exception as e:
        logging.error(f"Error handling command: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing the command."

    
    # Send the response back to the user
    await update.message.reply_text(response)
