from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import bot_handler as bot

app = Flask(__name__)

if __name__ == '__main__':
    bot.send_message()
    app.run(host='0.0.0.0', port=5020)
