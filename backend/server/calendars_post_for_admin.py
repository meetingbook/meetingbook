import uuid
from flask import make_response, jsonify, Blueprint
from server.auth import auth
from flask_httpauth import HTTPBasicAuth
from flask_expects_json import expects_json
from server.validation.schemas import calendar_link_schema

calendars_post = Blueprint('register_blueprint', __name__)



@calendars_post.route('/calendars', methods=['POST'])
@auth.login_required
@expects_json(calendar_link_schema)
def generate_calendar_link_id():
    link_for_calendars = uuid.uuid4()
    return jsonify({"calendars_id": link_for_calendars})

def generate_expiry_date_calendar_link_id():

    return jsonify({"valid_until": valid_until})


@error_handler(ValueError)
def value_error():
    return make_response({
        "status": 400,
        "detail": "Invalid format string"
    }, 400)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'status': 401, 'detail': 'Unauthorized'}), 401)