from app.model.merchant import Merchants
from app import response,db
from flask import request,jsonify
from app import db

def store():
    try:
        name        = request.json['name']
        image       = request.json['image']
        address     = request.json['address']
        rating      = request.json['rating']

        merchant     = Merchants(name=name, image=image, address=address, rating=rating)
        db.session.add(merchant)
        db.session.commit()
        return response.ok('', 'Successfully create Merchant !')
    except Exception as e:
        print(e)

def index():
    try:
        merchant    = Merchants.query.all()
        data       = transform(merchant)
        return response.ok(data,"Data Merchant Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        name        = request.json['name']
        image       = request.json['image']
        address     = request.json['address']
        rating      = request.json['rating']

        merchant          = Merchants.query.filter_by(id = id).first()
        merchant.name     = name
        merchant.image    = image
        merchant.address  = address
        merchant.rating   = rating

        db.session.commit()
        return response.ok('', 'Successfully update Merchant !')
    except Exception as e:
        print(e)

def show(id):
    try:
        merchant = Merchants.query.filter_by(id=id).first()
        if not merchant:
            return response.badRequest([], 'Empty....')
        data = singleTransform(merchant)
        return response.ok(data,"Data Merchant Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        merchant = Merchants.query.filter_by(id = id).first()
        if not merchant:
            return response.badRequest([], 'Empty....')
        db.session.delete(merchant)
        db.session.commit()
        return response.ok('', 'Successfully delete Merchant !')
    except Exception as e:
        print(e)


def transform(merchant):
    array = []
    for i in merchant:
        array.append(singleTransform(i))
    return array


def singleTransform(merchant):
    data = {
        'id' : merchant.id,
        'name'          : merchant.name,
        'image'         : merchant.image,
        'address'       : merchant.address,
        'rating'        : merchant.rating,
        'created_at'    : product.created_at,
        'updated_at'    : product.updated_at
    }

    return data