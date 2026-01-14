from app import db

class Habit(db.Model):
    __tablename__ = 'habits'
    friend_id = db.Column(db.Integer, primary_key=True)
    habit_name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    last_seen = db.Column(db.Date)
