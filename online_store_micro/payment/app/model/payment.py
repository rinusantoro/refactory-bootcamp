from app import db
from datetime import datetime

class Payments(db.Model):
    id              = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    payment_type    = db.Column(db.String(50), nullable=False)
    gross_amount    = db.Column(db.Integer, nullable=False)
    bank            = db.Column(db.String(15), foreign_key=True, nullable=False)
    order_id        = db.Column(db.Integer, nullable=False)
    created_at      = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at      = db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self):
        return '<Payment {}>'.format(self.payment_type)