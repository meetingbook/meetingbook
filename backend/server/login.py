from flask import Blueprint, make_response, jsonify
from flask_httpauth import HTTPBasicAuth

from domain.repositories.admin_repository import AdminDbRepository
from tools.func_for_psw import check_psw
auth = HTTPBasicAuth()
login_page = Blueprint('login_page', __name__)


@login_page.route('/login/', methods=['GET'])
@auth.login_required
def login():
    return "successful login, your email: {}!".format(auth.current_user())


@auth.verify_password
def verify_password(username, password):
    try:
        if check_psw(password, AdminDbRepository().get_psw_from_db(username)):
            return username
    except AttributeError:
        # user with this email does not exist
        return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
