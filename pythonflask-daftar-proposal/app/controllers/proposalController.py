from app.model.proposal import Proposals
from app import response,db
from flask import request,jsonify
from app.controllers import prodiController, userController
from app import db
from flask_jwt_extended import *

import datetime
from app import mail
from flask_mail import Message
from flask import render_template

def store():
    try:
        tgl_daftar = request.json['tgl_daftar']
        nim = request.json['nim']
        nama_mhs = request.json['nama_mhs']
        jml_sks = request.json['jml_sks']
        jml_ipk = request.json['jml_ipk']
        judul = request.json['judul']
        pembimbing = request.json['pembimbing']
        prodi_id = request.json['prodi_id']
        email = request.json['email']

        proposal = Proposals(tgl_daftar=tgl_daftar, nim=nim, nama_mhs=nama_mhs, jml_sks=jml_sks, jml_ipk=jml_ipk,judul=judul, pembimbing=pembimbing,prodi_id=prodi_id, email=email )
        db.session.add(proposal)
        db.session.commit()

        msg = Message(f"Hello, {nama_mhs} Welcome to Sistem Pendaftaran Proposal Online",
                      sender="bluut022@gmail.com")
        msg.add_recipient(email)
        message_value = f"INFORMASI!!! Pendaftaran Proposal Online atas nama: {nama_mhs} dengan NIM: {nim} telah pihak Kampus terima. Terima kasih."
        msg.html = render_template('email.html',message_key=message_value)

        mail.send(msg)
      
        return response.ok('', 'Successfully Create Daftar Proposal !')

    except Exception as e:
        print(e)

@jwt_required
def index():
    try:
        id = request.args.get('prodi_id')
        proposal = Proposals.query.filter_by(prodi_id = id).all()
        data = transform(proposal)
        return response.ok(data,"Data Daftar Proposal Skripsi Ditemukan!")
    except Exception as e:
        print(e)

@jwt_required
def update(id):
    try:
        tgl_daftar = request.json['tgl_daftar']
        nim = request.json['nim']
        nama_mhs = request.json['nama_mhs']
        jml_sks = request.json['jml_sks']
        jml_ipk = request.json['jml_ipk']
        judul = request.json['judul']
        pembimbing = request.json['pembimbing']
        prodi_id = request.json['prodi_id']
        email = request.json['email']

        proposal = Proposals.query.filter_by(id = id).first()
        proposal.tgl_daftar = tgl_daftar
        proposal.nim = nim
        proposal.nama_mhs = nama_mhs
        proposal.jml_sks = jml_sks
        proposal.jml_ipk = jml_ipk
        proposal.judul = judul
        proposal.pembimbing = pembimbing
        proposal.prodi_id = prodi_id
        proposal.email = email

        db.session.commit()
        return response.ok('', 'Successfully update Daftar Proposal Skripsi !')
    except Exception as e:
        print(e)

def show(id):
    try:
        proposal = Proposals.query.filter_by(id=id).first()
        if not proposal:
            return response.badRequest([], 'Empty....')
        data = singleTransform(proposal)
        return response.ok(data,"Data Daftar Proposal Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        proposal = Proposals.query.filter_by(id = id).first()
        if not proposal:
            return response.badRequest([], 'Empty....')
        db.session.delete(proposal)
        db.session.commit()
        return response.ok('', 'Successfully delete Daftar Proposal !')
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    print(values.prodis.id)
    print(values.prodis.nama_prodi)
    print(values.prodis.fakultas)
    data = {
        'id' : values.id,
        'user_id': values.prodi_id,
        'tgl_daftar': values.tgl_daftar,
        'nim': values.nim,
        'nama_mhs': values.nama_mhs,
        'jml_sks': values.jml_sks,
        'jml_ipk': values.jml_ipk,
        'judul': values.judul,
        'pembimbing': values.pembimbing,
        'email': values.email,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
        'prodi': prodiController.singleTransform(values.prodis, withProposal=False)
    }

    return data