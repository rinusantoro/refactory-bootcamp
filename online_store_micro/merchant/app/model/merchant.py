from app import db
from datetime import datetime

class Merchants(db.Model):
    id           = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    name         = db.Column(db.String(100), nullable=False)
    image        = db.Column(db.Text, nullable=False)
    address      = db.Column(db.String(150), nullable=False)
    rating       = db.Column(db.Integer, nullable=False)
    created_at   = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self):
        return '<Merchant {}>'.format(self.name)