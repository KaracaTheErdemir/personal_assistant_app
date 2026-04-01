from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config_manager import get_database_config

cfg = get_database_config()

DATABASE_URL = (
    f"postgresql+psycopg://{cfg['user']}:{cfg['password']}"
    f"@{cfg['host']}:{cfg['port']}/{cfg['database']}"
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()