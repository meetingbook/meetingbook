from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from tools.func_for_psw import check_psw
from tools.work_with_db import get_psw_from_db
auth = HTTPBasicAuth()
login_page = Blueprint('login_page', __name__)


@login_page.route('/login/', methods=['GET'])
@auth.login_required
def login():
    return "successful login, your email: {}!".format(auth.current_user())


@auth.verify_password
def verify_password(username, password):
    try:
        if check_psw(password, get_psw_from_db(username)):
            return username
    except AttributeError:
        # user with this email does not exist
        auth.login_required()
