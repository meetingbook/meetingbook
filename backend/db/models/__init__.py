from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_marshmallow import Marshmallow
from sqlalchemy.sql.sqltypes import JSON
db = SQLAlchemy()
ma = Marshmallow()


class AdminInfo(db.Model):
    __tablename__ = 'AdminInfo'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    psw = db.Column(db.String(500), nullable=False)
    slots = db.relationship('Slots', backref='admin_slot', lazy='dynamic')
    booking_settings = db.relationship('BookingSettings',
                                       backref='admin_booking_settings',
                                       lazy='dynamic')
    links = db.relationship('Links', backref='admin_link')


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


class BookingSettings(db.Model):
    __tablename__ = 'BookingSettings'
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(JSON(), nullable=False)
    start_time = db.Column(JSON(), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('AdminInfo.id'))


class Links(db.Model):
    __tablename__ = 'Links'
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.String(100), unique=True, nullable=False)
    valid_until = db.Column(db.String(50), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('AdminInfo.id'))


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


class BookingSettingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookingSettings
        load_instance = True
    id = ma.auto_field()
    start_time = ma.auto_field()
    duration = ma.auto_field()


class LinksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Links
        load_instance = True
    id = ma.auto_field()
    link_id = ma.auto_field()
    valid_until = ma.auto_field()
