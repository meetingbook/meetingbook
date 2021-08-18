from flask import Flask, jsonify
from server.hello_json import msg_hello
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////meetingbook/backend/db/main_db.sqlite'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AdminInfo(db.Model):
    __tablename__ = 'AdminInfo'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    psw = db.Column(db.String(500), nullable=False)


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
    start_interval = db.Column(db.String(50), unique=True, nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('BookingInfo.id'))


@app.route("/", methods=["GET"])
def index():
    return jsonify(hello=msg_hello)


if __name__ == "__main__":
    app.run(debug=True)
