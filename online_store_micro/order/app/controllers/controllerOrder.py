from app.model.order import Orders
from app import response,db
from flask import request,jsonify
from app import db

def store():
    try:
        product_id   = request.json['product_id']
        quantity     = request.json['quantity']

        order        = Orders(product_id=product_id, quantity=quantity)
        db.session.add(order)
        db.session.commit()
        return response.ok('', 'Successfully create Order !')
    except Exception as e:
        print(e)

def index():
    try:
        id      = request.args.get('id')
        order   = Orders.query.filter_by(id = id).all()
        data    = transform(order)
        return response.ok(data,"Data Order Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        product_id   = request.json['product_id']
        quantity     = request.json['quantity']

        order             = Orders.query.filter_by(id = id).first()
        order.product_id  = product_id
        order.quantity    = quantity

        db.session.commit()
        return response.ok('', 'Successfully update Order !')
    except Exception as e:
        print(e)

def show(id):
    try:
        order = Orders.query.filter_by(id=id).first()
        if not order:
            return response.badRequest([], 'Empty....')
        data = singleTransform(order)
        return response.ok(data,"Data Order Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        order = Orders.query.filter_by(id = id).first()
        if not order:
            return response.badRequest([], 'Empty....')
        db.session.delete(order)
        db.session.commit()
        return response.ok('', 'Successfully delete Order !')
    except Exception as e:
        print(e)


def transform(order):
    array = []
    for i in order:
        array.append(singleTransform(i))
    return array


def singleTransform(order):
    data = {
        'id' : order.id,
        'product_id': order.product_id,
        'quantity': order.quantity,
        'created_at': order.created_at,
        'updated_at': order.updated_at
    }

    return data