from app import db
from datetime import datetime

class Products(db.Model):
    id           = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    name         = db.Column(db.String(100), nullable=False)
    price        = db.Column(db.Integer, nullable=False)
    created_at   = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self):
        return '<Product {}>'.format(self.name)