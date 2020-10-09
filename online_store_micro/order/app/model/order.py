from app import db
from datetime import datetime

class Orders(db.Model):
    id          = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    product_id  = db.Column(db.BigInteger, nullable=False)
    quantity    = db.Column(db.Integer, nullable=False)
    created_at  = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self):
        return '<Order {}>'.format(self.quantity)