from flask import make_response, jsonify
from domain.repositories.admin_repository import AdminDbRepository
from tools.func_for_psw import check_psw
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


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
