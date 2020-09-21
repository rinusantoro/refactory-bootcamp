from app import db
from datetime import datetime
from app.model.prodi import Prodis

class Proposals(db.Model):
    id          = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    tgl_daftar  = db.Column(db.Date, nullable=False)
    nim         = db.Column(db.String(10), unique=True, nullable=False)
    nama_mhs    = db.Column(db.String(100), nullable=False)
    jml_sks     = db.Column(db.String(5), nullable=True)
    jml_ipk     = db.Column(db.String(5), nullable=True)
    judul       = db.Column(db.String(150), nullable=True)
    pembimbing  = db.Column(db.String(150), nullable=True)
    email       = db.Column(db.String(120),index=True,unique=True,nullable=False)
    created_at  = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime,default=datetime.utcnow)
    prodi_id    = db.Column(db.BigInteger,db.ForeignKey(Prodis.id))
    prodis      = db.relationship("Prodis",backref="prodi_id")


def __repr__(self):
        return '<Prodi {}>'.format(self.nama_prodi)