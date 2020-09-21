from app import app
from app.controllers import prodiController
from flask import request


@app.route('/prodi', methods=['POST','GET'])
def prodi():
    if request.method == 'POST':
        return prodiController.store()
    elif request.method == 'GET':
        return prodiController.index()


@app.route('/prodi/<id>', methods=['PUT','GET','DELETE'])
def prodiDetail(id):
    if request.method == 'GET':
        return prodiController.show(id)
    elif request.method == 'PUT':
        return prodiController.update(id)
    elif request.method == 'DELETE':
        return prodiController.delete(id)