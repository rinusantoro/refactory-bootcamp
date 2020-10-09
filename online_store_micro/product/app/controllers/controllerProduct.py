from app.model.product import Products
from app import response,db
from flask import request,jsonify
from app import db

def store():
    try:
        name        = request.json['name']
        price       = request.json['price']

        product     = Products(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        return response.ok('', 'Successfully create Product !')
    except Exception as e:
        print(e)

def index():
    try:
        product    = Products.query.all()
        data       = transform(product)
        return response.ok(data,"Data Product Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        name        = request.json['name']
        price       = request.json['price']

        product          = Products.query.filter_by(id = id).first()
        product.name     = name
        product.price    = price

        db.session.commit()
        return response.ok('', 'Successfully update Product !')
    except Exception as e:
        print(e)

def show(id):
    try:
        product = Products.query.filter_by(id=id).first()
        if not product:
            return response.badRequest([], 'Empty....')
        data = singleTransform(product)
        return response.ok(data,"Data Product Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        product = Products.query.filter_by(id = id).first()
        if not product:
            return response.badRequest([], 'Empty....')
        db.session.delete(product)
        db.session.commit()
        return response.ok('', 'Successfully delete Product !')
    except Exception as e:
        print(e)


def transform(product):
    array = []
    for i in product:
        array.append(singleTransform(i))
    return array


def singleTransform(product):
    data = {
        'id' : product.id,
        'name'          : product.name,
        'price'         : product.price,
        'created_at'    : product.created_at,
        'updated_at'    : product.updated_at
    }

    return data