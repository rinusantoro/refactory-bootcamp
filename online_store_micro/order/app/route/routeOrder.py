from app import app
from app.controllers import controllerOrder
from flask import request


@app.route('/order', methods=['POST','GET'])
def order():
    if request.method == 'POST':
        return controllerOrder.store()
    elif request.method == 'GET':
        return controllerOrder.index()


@app.route('/order/<id>', methods=['PUT','GET','DELETE'])
def orderDetail(id):
    if request.method == 'GET':
        return controllerOrder.show(id)
    elif request.method == 'PUT':
        return controllerOrder.update(id)
    elif request.method == 'DELETE':
        return controllerOrder.delete(id)