from flask import Flask, jsonify
from server.hello_json import msg_hello
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////meetingbook/backend/db/main_db.sqlite'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AdminInfo(db.Model):
    __tablename__ = 'admin_info'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500))


class BookingInfo(db.Model):
    __tablename__ = 'booking_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(500))
    topic = db.Column(db.String(500))
    slots_inf = db.relationship('Slots', backref='info', lazy='dynamic')


class Slots(db.Model):
    __tablename__ = 'slots'
    id = db.Column(db.Integer, primary_key=True)
    start_interval = db.Column(db.String(50), unique=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking_info.id'))


@app.route("/", methods=["GET"])
def index():
    return jsonify(hello=msg_hello)


if __name__ == "__main__":
    app.run(debug=True)
