from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from db import Base

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    priority = Column(Integer, default=3)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)