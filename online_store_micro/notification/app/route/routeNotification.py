from app import app
from app.controllers import controllerNotification
from flask import request


@app.route('/notif', methods=['POST','GET'])
def notif():
    if request.method == 'POST':
        return controllerNotification.store()
    elif request.method == 'GET':
        return controllerNotification.index()


@app.route('/notif/<id>', methods=['PUT','GET','DELETE'])
def notifDetail(id):
    if request.method == 'GET':
        return controllerNotification.show(id)
    elif request.method == 'PUT':
        return controllerNotification.update(id)
    elif request.method == 'DELETE':
        return controllerNotification.delete(id)