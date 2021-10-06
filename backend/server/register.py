from flask import Blueprint, request, jsonify, make_response

from tools.func_for_psw import password_hashing
from tools.for_db.work_with_admin_info import AdminExistsException, add_admin
from tools.validation import InvalidPasswordException, InvalidEmailException, email_validation, password_validation

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/registration', methods=['POST'])
def registration():
    try:
        request_body = request.get_json()
        checked_email = email_validation(request_body['email'])
        checked_password = password_validation(request_body['password'])
        hashed_password = password_hashing(checked_password)
        add_admin(checked_email, hashed_password)
    except AdminExistsException:
        return make_response(jsonify({"status": 409,
                                      'detail': 'Conflict. This email is already registered in MeetingBook'}), 409)
    except (InvalidPasswordException, InvalidEmailException) as e:
        return make_response(jsonify({"status": 400, "detail": f"Bad request. Invalid value {e}"}),
                             400)
    except (KeyError, TypeError):
        return make_response(jsonify({"status": 400, "detail": "Bad request. Missing required fields"}),
                             400)
    return jsonify({'detail': 'Successful registration'})
