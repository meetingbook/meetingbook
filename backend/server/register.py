from flask import Blueprint, request, jsonify, make_response
from flask_expects_json import expects_json
from server.validation.schemas import register_schema

from tools.func_for_psw import password_hashing
from tools.for_db.work_with_admin_info import AdminExistsException, add_admin

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/registration', methods=['POST'])
@expects_json(register_schema)
def registration():
    try:
        email, password = request.get_json().values()
        hashed_password = password_hashing(password)
        add_admin(email, hashed_password)
    except AdminExistsException:
        return make_response(jsonify({"status": 409,
                                      'detail': 'Conflict. This email is already registered in MeetingBook'}), 409)
    return jsonify({'detail': 'Successful registration'})
