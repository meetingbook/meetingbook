from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
db = SQLAlchemy()


@dataclass
class AdminInfo(db.Model):
    id: int
    email: str
    psw: str
    slots: 'Slots'

    __tablename__ = 'AdminInfo'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    psw = db.Column(db.String(500), nullable=False)
    slots = db.relationship('Slots', backref='admin_slot', lazy='dynamic')


@dataclass
class BookingInfo(db.Model):
    id: int
    name: str
    email: str
    topic: str
    slots_inf: 'Slots'

    __tablename__ = 'BookingInfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    topic = db.Column(db.String(500))
    slots_inf = db.relationship('Slots', backref='info', lazy='dynamic')


@dataclass
class Slots(db.Model):
    id: int
    start_interval: str
    end_interval: str
    booking_id: int
    admin_id: int

    __tablename__ = 'Slots'
    id = db.Column(db.Integer, primary_key=True)
    start_interval = db.Column(db.String(50), nullable=False)
    end_interval = db.Column(db.String(50), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('BookingInfo.id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('AdminInfo.id'))
    UniqueConstraint(start_interval, end_interval, admin_id)
