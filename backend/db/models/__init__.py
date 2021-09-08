from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()


class AdminInfo(db.Model):
    __tablename__ = 'AdminInfo'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    psw = db.Column(db.String(500), nullable=False)
    slots = db.relationship('Slots', backref='admin_slot', lazy='dynamic')


class BookingInfo(db.Model):
    __tablename__ = 'BookingInfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    topic = db.Column(db.String(500))
    slots_inf = db.relationship('Slots', backref='info', lazy='dynamic')


class Slots(db.Model):
    __tablename__ = 'Slots'
    id = db.Column(db.Integer, primary_key=True)
    start_interval = db.Column(db.String(50), nullable=False)
    end_interval = db.Column(db.String(50), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('BookingInfo.id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('AdminInfo.id'))
    UniqueConstraint(start_interval, end_interval, admin_id)
