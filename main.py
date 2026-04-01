import asyncio
from db import engine, Base
import models  # VERY IMPORTANT

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from handlers.bot_handler import start_bot

app = Flask(__name__)

def create_tables():
    Base.metadata.create_all(bind=engine)
    
def main():
    # asyncio.run(start_bot())
    create_tables()
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    loop.run_forever()
    app.run(host='0.0.0.0', port=5020)
    
if __name__ == '__main__':
    main()

