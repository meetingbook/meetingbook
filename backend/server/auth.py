from flask import make_response, jsonify
from flask_httpauth import HTTPBasicAuth

from tools.func_for_psw import check_psw
from tools.for_db.work_with_admin_info import get_psw_from_db

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    try:
        if check_psw(password, get_psw_from_db(username)):
            return username
    except AttributeError:
        # user with this email does not exist
        return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'status': 401, 'detail': 'Unauthorized'}), 401)
