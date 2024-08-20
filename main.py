import asyncio

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from handlers.bot_handler import start_bot

app = Flask(__name__)

def main():
    # asyncio.run(start_bot())
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    loop.run_forever()
    app.run(host='0.0.0.0', port=5020)
    
if __name__ == '__main__':
    main()

