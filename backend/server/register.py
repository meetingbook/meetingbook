from flask import Blueprint, request
from flask_expects_json import expects_json
from server.validation.schemas import register_schema
from tools.for_db.work_with_booking_settings import AdminDefaulSettings
from tools.func_for_psw import password_hashing
from tools.for_db.work_with_admin_info import AdminExistsException, add_admin
from tools.build_response import build_response
register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/registration', methods=['POST'])
@expects_json(register_schema)
def registration():
    try:
        email, password = request.get_json().values()
        hashed_password = password_hashing(password)
        add_admin(email, hashed_password)
    except AdminExistsException:
        return build_response('Conflict. This email is already registered in MeetingBook', 409)
    except AdminDefaulSettings as e:
        return build_response(f'{e}', 500)
    return build_response('Successful registration', 200)
