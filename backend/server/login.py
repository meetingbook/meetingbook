from flask import Blueprint
from server.auth import auth

login_page = Blueprint('login_page', __name__)


@login_page.route('/login/', methods=['GET'])
@auth.login_required
def login():
    return "successful login, your email: {}!".format(auth.current_user())
