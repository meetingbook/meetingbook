from flask import Blueprint, jsonify

from server.auth import auth

login_page = Blueprint('login_page', __name__)


@login_page.route('/login', methods=['GET'])
@auth.login_required
def login():
    return jsonify({'detail': 'Successful login'})
