from app import app
from app.controllers import controllerPayment
from flask import request


@app.route('/payment', methods=['POST','GET'])
def payment():
    if request.method == 'POST':
        return controllerPayment.store()
    elif request.method == 'GET':
        return controllerPayment.index()


@app.route('/payment/<id>', methods=['PUT','GET','DELETE'])
def paymentDetail(id):
    if request.method == 'GET':
        return controllerPayment.show(id)
    elif request.method == 'PUT':
        return controllerPayment.update(id)
    elif request.method == 'DELETE':
        return controllerPayment.delete(id)