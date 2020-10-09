from app import db
from datetime import datetime

class Notifications(db.Model):
    id           = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title        = db.Column(db.String(100), nullable=False)
    message      = db.Column(db.String(150), nullable=False)
    tipe         = db.Column(db.String(50), nullable=False)
    dari         = db.Column(db.String(50), nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
        return '<Notification {}>'.format(self.title)