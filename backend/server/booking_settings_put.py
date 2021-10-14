from flask import Blueprint, request
from server.auth import auth
from tools.put_booking_settings import put_booking_settings
from flask_expects_json import expects_json
from server.validation.schemas import booking_settings_schema

booking_settings_put = Blueprint('booking_settings_put', __name__)


@booking_settings_put.route('/booking_settings', methods=['PUT'])
@expects_json(booking_settings_schema)
@auth.login_required
def booking_settings():
    email_admin = auth.current_user()
    duration, start_time = request.get_json().values()
    return put_booking_settings(duration, start_time, email_admin)
