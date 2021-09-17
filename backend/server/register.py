from flask import Blueprint, request, jsonify
from tools.work_with_db import get_psw_from_db

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def registration():
    email = request.form['email']
    psw = request.form['psw']
    psw2 = request.form['psw2']
    try:
        get_psw_from_db(email)
        return jsonify({'error': 'such user already exists'})
    except AttributeError:
        if psw != psw2:
            return jsonify({'error': 'Password mismatch'})


