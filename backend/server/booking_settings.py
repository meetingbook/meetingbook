from flask import Blueprint, jsonify
from db.models import BookingSettings, BookingSettingsSchema
from server.auth import auth

booking_settings_blueprint = Blueprint('booking_settings_blueprint', __name__)


@booking_settings_blueprint.route('/booking_settings', methods=['GET'])
@auth.login_required
def get_booking_settings():
    # TODO query booking setting for a particular admin.
    # You can get admin by Authentication header
    booking_settings = BookingSettings.query.all()
    booking_settings_json = BookingSettingsSchema(many=True).dump(booking_settings)
    response = jsonify({"booking_settings": booking_settings_json})

    return response
