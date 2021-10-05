from tools.for_db.work_with_admin_info import AdminExistsException
from flask import Blueprint, request, redirect, jsonify, make_response

from domain.entities.email import InvalidEmailException
from domain.value_objects.password import InvalidPasswordException
from domain.use_cases.admin_usecases import AdminRegister

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def registration():
    try:
        email = request.form['email']
        psw = request.form['password']
        AdminRegister(email, psw).admin_register()
    except AdminExistsException:
        return make_response(jsonify({'detail': 'Conflict. This email is already registered in MeetingBook'}), 409)
    except (InvalidPasswordException, InvalidEmailException, KeyError):
        return make_response(jsonify({"detail": "Bad request. This is not a valid email or password is not specified"}),
                             400)
    else:
        return redirect('/login/', code=200)
