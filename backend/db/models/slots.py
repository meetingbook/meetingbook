from db.models import db


class Slots(db.Model):
    __tablename__ = 'Slots'
    id = db.Column(db.Integer, primary_key=True)
    start_interval = db.Column(db.String(50), unique=True, nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('BookingInfo.id'))
