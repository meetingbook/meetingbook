from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from tools.build_response import build_response
admin_page = Blueprint('admin_page', __name__)
auth = HTTPBasicAuth()


@admin_page.route("/admin", methods=['GET'])
@auth.login_required
def admin():
    return {'message': 'OK'}


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'Pyth0n'
    return None


@auth.error_handler
def unauthorized():
    return build_response('Unauthorized access', 401)
