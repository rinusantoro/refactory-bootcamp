from app import db
from datetime import datetime
from app.model.user import Users

class Prodis(db.Model):
    id          = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    nama_prodi  = db.Column(db.String(140), unique=True, nullable=False)
    fakultas    = db.Column(db.String(100), unique=False, nullable=False)
    created_at  = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime,default=datetime.utcnow)
    user_id     = db.Column(db.BigInteger,db.ForeignKey(Users.id))
    users       = db.relationship("Users",backref="user_id")
    proposals   = db.relationship("Proposals",
                                  lazy    ='select',
                                  backref =db.backref('proposals',lazy ='joined'))

def __repr__(self):
        return '<Prodi {}>'.format(self.nama_prodi)