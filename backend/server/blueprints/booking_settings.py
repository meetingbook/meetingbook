from flask import Blueprint, jsonify
from server.endpoints_func.get_booking_settings import get_booking_settings
from server.auth import auth


booking_settings_blueprint = Blueprint('booking_settings_blueprint', __name__)


@booking_settings_blueprint.route('/booking_settings', methods=['GET'])
@auth.login_required
def booking_settings():
    empty_response = {
        "duration": {},
        "start_time": {}
    }
    email_admin = auth.current_user()
    settings = get_booking_settings(email_admin)
    return empty_response if settings == [] else jsonify(settings)
