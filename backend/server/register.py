from flask import Blueprint, request, redirect, jsonify, make_response

from tools.func_for_psw import password_hashing
from tools.for_db.work_with_admin_info import AdminExistsException, add_admin
from tools.validation import InvalidPasswordException, InvalidEmailException, email_validation, password_validation

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def registration():
    try:
        email = request.form['email']
        password = request.form['password']
        checked_email = email_validation(email)
        checked_password = password_validation(password)
        hashed_password = password_hashing(checked_password)
        add_admin(checked_email, hashed_password)
    except AdminExistsException:
        return make_response(jsonify({'detail': 'Conflict. This email is already registered in MeetingBook'}), 409)
    except (InvalidPasswordException, InvalidEmailException) as e:
        return make_response(jsonify({"detail": f"Bad request. Invalid value {e}"}),
                             400)
    except KeyError:
        return make_response(jsonify({"detail": "Bad request. Missing required field"}),
                             400)
    else:
        return redirect('/login/', code=200)
