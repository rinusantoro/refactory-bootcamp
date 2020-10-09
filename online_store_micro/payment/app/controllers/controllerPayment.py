from app.model.payment import Payments
from app import response,db
from flask import request,jsonify
from app import db

def store():
    try:
        payment_type    = request.json['payment_type']
        gross_amount    = request.json['gross_amount']
        bank            = request.json['bank']
        order_id        = request.json['order_id']

        payment        = Payments(payment_type=payment_type, gross_amount=gross_amount, bank=bank, order_id=order_id)
        db.session.add(payment)
        db.session.commit()
        return response.ok('', 'Successfully create Payment !')
    except Exception as e:
        print(e)

def index():
    try:
        id          = request.args.get('id')
        payment     = Orders.query.filter_by(id = id).all()
        data        = transform(payment)
        return response.ok(data,"Data Payment Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        payment_type    = request.json['payment_type']
        gross_amount    = request.json['gross_amount']
        bank            = request.json['bank']
        order_id        = request.json['order_id']

        payment                 = Payments.query.filter_by(id = id).first()
        payment.payment_type    = payment_type
        payment.gross_amount    = gross_amount
        payment.bank            = bank
        payment.order_id        = order_id

        db.session.commit()
        return response.ok('', 'Successfully update Payment !')
    except Exception as e:
        print(e)

def show(id):
    try:
        payment = Payments.query.filter_by(id=id).first()
        if not payment:
            return response.badRequest([], 'Empty....')
        data = singleTransform(payment)
        return response.ok(data,"Data Payment Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        payment = Payments.query.filter_by(id = id).first()
        if not payment:
            return response.badRequest([], 'Empty....')
        db.session.delete(payment)
        db.session.commit()
        return response.ok('', 'Successfully delete Payment !')
    except Exception as e:
        print(e)


def transform(payment):
    array = []
    for i in payment:
        array.append(singleTransform(i))
    return array


def singleTransform(payment):
    data = {
        'id' : payment.id,
        'payment_type': payment.payment_type,
        'gross_amount': payment.gross_amount,
        'bank'        : payment.bank,
        'order_id'    : payment.order_id,
        'created_at'  : payment.created_at,
        'updated_at'  : payment.updated_at
    }

    return data