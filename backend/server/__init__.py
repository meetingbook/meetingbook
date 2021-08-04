from flask import Flask
from db import booking_info
from flask import jsonify

app = Flask(__name__)


@app.route("/api/bookings", methods=["GET"])
def all_bookings():
    response = jsonify(bookings=booking_info)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/api/bookings/<booking_id>", methods=["GET"])
def get_booking(booking_id):
    booking = list(
        filter(lambda x: x["id"] == int(booking_id), booking_info)
    )
    return {"booking": booking}


@app.route("/api/bookings", methods=["POST"])
def create_booking(booking):
    pass


@app.route("/api/bookings", methods=["PUT"])
def update_booking(booking):
    pass


@app.route("/api/bookings", methods=["DELETE"])
def delete_all_booking():
    pass


@app.route("/api/bookings/<booking_d>", methods=["DELETE"])
def delete_booking(booking_d):
    pass


if __name__ == '__main__':
    app.run(debug=True)
