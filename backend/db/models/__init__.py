from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()


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


class AdminInfoShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdminInfo
        load_instance = True
    id = ma.auto_field()
    email = ma.auto_field()
    psw = ma.auto_field()
    slots = ma.auto_field()


class BookingInfoShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookingInfo
        load_instance = True
    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    topic = ma.auto_field()
    slots_inf = ma.auto_field()


class SlotsShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Slots
        load_instance = True
    id = ma.auto_field()
    start_interval = ma.auto_field()
    end_interval = ma.auto_field()
    booking_id = ma.auto_field()
