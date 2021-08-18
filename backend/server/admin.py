from flask import jsonify, make_response, Blueprint
from flask_httpauth import HTTPBasicAuth

admin_page = Blueprint('admin_page', __name__)
auth = HTTPBasicAuth()


@admin_page.route("/admin")
@auth.login_required
def admin():
    return "OK"


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'Pyth0n'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
