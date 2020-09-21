from app.model.prodi import Prodis
from app import response,db
from flask import request,jsonify
from app.controllers import userController
from app import db

def store():
    try:
        nama_prodi = request.json['nama_prodi']
        fakultas = request.json['fakultas']
        user_id = request.json['user_id']

        prodi = Prodis(user_id=user_id, nama_prodi=nama_prodi, fakultas = fakultas)
        db.session.add(prodi)
        db.session.commit()
        
        return response.ok('', 'Successfully create Prodi !')
    except Exception as e:
        print(e)

def index():
    try:
        id = request.args.get('user_id')
        prodi = Prodis.query.filter_by(user_id = id).all()
        data = transform(prodi)
        return response.ok(data,"Data Prodi Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        inputProdi = request.json['nama_prodi']
        inputFak = request.json['fakultas']
        prodi = Prodis.query.filter_by(id = id).first()
        prodi.nama_prodi = inputProdi
        prodi.fakultas = inputFak
        db.session.commit()
        return response.ok('', 'Successfully update todo !')
    except Exception as e:
        print(e)

def show(id):
    try:
        prodi = Prodis.query.filter_by(id=id).first()
        if not prodi:
            return response.badRequest([], 'Empty....')
        data = singleTransform(prodi)
        return response.ok(data,"Data Prodi Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        prodi = Prodis.query.filter_by(id = id).first()
        if not todo:
            return response.badRequest([], 'Empty....')
        db.session.delete(prodi)
        db.session.commit()
        return response.ok('', 'Successfully delete Prodi !')
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values, withProposal=True):
    print(values.users.id)
    print(values.users.email)
    data = {
        'id' : values.id,
        'user_id': values.user_id,
        'nama_prodi': values.nama_prodi,
        'fakultas': values.fakultas,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
        'user': userController.singleTransform(values.users, withProdi=False)
    }

    if withProposal:
        proposals = []
        for i in prodis.proposals:
            proposals.append({
                'id':i.id,
                'tgl_daftar': i.tgl_daftar,
                'nim': i.nim,
                'nama_mhs': i.nama_mhs,
                'jml_sks': i.jml_sks,
                'jml_ipk': i.jml_ipk,
                'judul': i.judul,
                'pembimbing': i.pembimbing
            })
            data['proposals'] = proposals


    return data