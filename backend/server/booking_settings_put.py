from flask import Blueprint, request
from server.auth import auth
from tools.put_booking_settings import put_booking_settings
from tools.build_response import build_response

booking_settings_put = Blueprint('booking_settings_put', __name__)


@booking_settings_put.route('/booking_settings', methods=['PUT'])
@auth.login_required
def booking_settings():
    email_admin = auth.current_user()
    try:
        duration, start_time = request.get_json().values()
        return put_booking_settings(duration, start_time, email_admin)
    except ValueError as e:
        return build_response(e, 500)
