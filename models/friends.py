from app import db

class Friend(db.Model):
    __tablename__ = 'friends'
    friend_id = db.Column(db.Integer, primary_key=True)
    friend_name = db.Column(db.String(50))
    sex = db.Column(db.String(10))
    profession = db.Column(db.String(50))
    meet_score = db.Column(db.Integer)
    last_seen = db.Column(db.Date)
