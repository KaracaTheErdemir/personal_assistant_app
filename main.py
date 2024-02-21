import asyncio

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bot_handler import start_bot

app = Flask(__name__)

def main():
    asyncio.run(start_bot())
    app.run(host='0.0.0.0', port=5020)

if __name__ == '__main__':
    main()

