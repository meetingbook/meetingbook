from flask import Blueprint, jsonify
from tools.get_booking_settings import get_booking_settings

'''Uncomment here and in the `get_booking_settings.py` file when the authentication check is added'''


booking_settings_blueprint = Blueprint('booking_settings_blueprint', __name__)


@booking_settings_blueprint.route('/booking_settings', methods=['GET'])
# @auth.login_required
def booking_settings():
    return jsonify(get_booking_settings())
    # email_admin = auth.current_user()
    # return jsonify(get_booking_settings(email_admin))
