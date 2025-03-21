import json
import sys
import os
import logging
import shlex

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
#sys.path.append(os.path.abspath('/Users/hermestrismegistus/per
# sonal_assistant_app'))
from config_manager import get_telegram_config
from handlers.command_handler import delete_expense, delete_friend, delete_habit, delete_meeting, delete_todo, list_expenses, list_friends, list_habits, list_meetings, list_todos, new_expense, new_friend, new_habit, new_meeting, new_todo, track_habit, track_todo, update_friend, update_habit, update_meeting, update_todo, help

config = get_telegram_config()
TELEGRAM_TOKEN = config['token']
CHAT_ID = config['chat_id']

async def send_message(message):
    # Create a Bot instance
    bot = Bot(token=TELEGRAM_TOKEN)
    # Send a message
    #unicode_message = message.encode('utf-8').decode('utf-8')

    await bot.send_message(chat_id=CHAT_ID, text=message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Call handle_command and get the return string
        response_message =  await handle_command(update, context)
        # Send the response back to the user
        await send_message(response_message)

    except Exception as e:
        logging.error(f"Error in handle_message: {type(e).__name__} - {str(e)}")
        await send_message(e)
        

async def start_bot():
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logging.getLogger('httpx').setLevel(logging.WARNING) # To avoid the flood of httpx info messages.

        app = Application.builder().token(TELEGRAM_TOKEN).build()
        # Add handlers to the Application
        app.add_handler(MessageHandler(filters.TEXT, handle_message))
        await send_message("I am alive.\nWelcome!")
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
        line = update.message.text
        arguments = shlex.split(line)
        
        command = arguments[0]
        if command != '/help':
            option = arguments[1]
        # Route the command and option to the appropriate function

        if command == '/new':
            if option == 'friend':
                return new_friend(arguments)
            elif option == 'meeting':
                return new_meeting(arguments)
            elif option == 'expense':
                return new_expense(arguments)
            elif option == 'habit':
                return new_habit(arguments)
            elif option == 'plan':
                return new_todo(arguments)
            else:
                return "Invalid option for /new."

        elif command == '/update':
            if option == 'friend':
                await send_message(f"updating friend {arguments[3]}")
                return update_friend(arguments)
            elif option == 'meeting':
                return update_meeting(arguments)
            elif option == 'habit':
                return update_habit(arguments)
            elif option == 'todo':
                return update_todo(arguments)
            else:
                return "Invalid option for /update."

        elif command == '/track':
            if option == 'habit':
                return track_habit(arguments)
            elif option == 'plan':
                return track_todo(arguments)
            else:
                return "Invalid option for /track."

        elif command == '/list':
            limit = arguments[2]
            if option == 'friends':
                result = list_friends(limit)
                return result
            elif option == 'meetings':
                result = list_meetings(limit)
                return result
            elif option == 'habits':
                return list_habits(limit)
            elif option == 'plans':
                return list_todos(limit)
            elif option == 'expenses':
                return list_expenses(limit)
            else:
                return "Invalid option for /list."
            
        elif command == '/delete':
            if option == 'friend':
                return delete_friend(arguments)
            elif option == 'meeting':
                result = delete_meeting(arguments)
                return result
            elif option == 'habit':
                return delete_habit(arguments)
            elif option == 'plan':
                return delete_todo(arguments)
            elif option == 'expense':
                return delete_expense(arguments)
            else:
                return "Invalid option for /delete."
        elif command == '/help':
            result = help()
            return result
        else:
            return "Unknown command."
    except Exception as e:
        logging.error(f"Error handling command: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing the command."

    
    # Send the response back to the user
    await update.message.reply_text(response)
