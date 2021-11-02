from flask_httpauth import HTTPBasicAuth
from tools.build_response import build_response
from tools.func_for_psw import check_psw
from tools.for_db.work_with_admin_info import get_psw_from_db

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    try:
        if check_psw(password, get_psw_from_db(email)):
            return email
    except AttributeError:
        # user with this email does not exist
        return None


@auth.error_handler
def unauthorized():
    return build_response('Unauthorized', 401)
