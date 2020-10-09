from app.model.notification import Notifications
from app import response,db
from flask import request,jsonify
from app import db

def store():
    try:
        title       = request.json['title']
        message     = request.json['message']
        tipe        = request.json['tipe']
        dari        = request.json['dari']

        notification= Notifications(title=title, message=message, tipe=tipe, dari=dari)
        db.session.add(notification)
        db.session.commit()
        return response.ok('', 'Successfully create Notification !')
    except Exception as e:
        print(e)

def index():
    try:
        notification = Notifications.query.all()
        data         = transform(notification)
        return response.ok(data,"Data Notification Ditemukan!")
    except Exception as e:
        print(e)

def update(id):
    try:
        title       = request.json['title']
        message     = request.json['message']
        tipe        = request.json['tipe']
        dari        = request.json['dari']

        notification          = Notifications.query.filter_by(id = id).first()
        notification.title    = title
        notification.message  = message
        notification.tipe     = tipe
        notification.dari     = dari

        db.session.commit()
        return response.ok('', 'Successfully update Notification !')
    except Exception as e:
        print(e)

def show(id):
    try:
        notification = Notifications.query.filter_by(id=id).first()
        if not notification:
            return response.badRequest([], 'Empty....')
        data = singleTransform(notification)
        return response.ok(data,"Data Notification Ditemukan!")
    except Exception as e:
        print(e)

def delete(id):
    try:
        notification = Notifications.query.filter_by(id = id).first()
        if not notification:
            return response.badRequest([], 'Empty....')
        db.session.delete(notification)
        db.session.commit()
        return response.ok('', 'Successfully delete Notification !')
    except Exception as e:
        print(e)


def transform(notification):
    array = []
    for i in notification:
        array.append(singleTransform(i))
    return array


def singleTransform(notification):
    data = {
        'id' : notification.id,
        'title'         : notification.title,
        'message'       : notification.message,
        'tipe'          : notification.tipe,
        'dari'          : notification.dari,
        'created_at'    : notification.created_at,
        'updated_at'    : notification.updated_at
    }

    return data