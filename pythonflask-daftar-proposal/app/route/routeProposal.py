from app import app
from app.controllers import proposalController, proposalFileController
from flask import request


@app.route('/daftar-proposal', methods=['POST','GET'])
def proposal():
    if request.method == 'POST':
        return proposalController.store()
    elif request.method == 'GET':
        return proposalController.index()


@app.route('/daftar-proposal/<id>', methods=['PUT','GET','DELETE'])
def proposalDetail(id):
    if request.method == 'GET':
        return proposalController.show(id)
    elif request.method == 'PUT':
        return proposalController.update(id)
    elif request.method == 'DELETE':
        return proposalController.delete(id)



@app.route('/proposal-files/<id>', methods=['POST','GET'])
def proposalFiles(id):
    if request.method == 'POST':
        return proposalFileController.store(id)
    if request.method == 'GET':
        return proposalFileController.index(id)