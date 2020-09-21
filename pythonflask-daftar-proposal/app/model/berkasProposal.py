from app import db
from datetime import datetime
from app.model.proposal import Proposals


class ProposalFiles(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_name = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    proposal_id = db.Column(db.BigInteger, db.ForeignKey(Proposals.id))
    proposals = db.relationship("Proposals", backref="proposal_id")


    def __repr__(self):
        return '<Proposal {}>'.format(self.nama_mhs)