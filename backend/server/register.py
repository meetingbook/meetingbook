import sqlalchemy
from flask import Blueprint, request, redirect, jsonify

from domain.use_cases.admin_usecases import AdminRegister

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def registration():
    email = request.form['email']
    psw = request.form['psw']
    try:
        AdminRegister(email, psw).admin_register()
        return redirect('/login/', code=401)
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'error': 'such user already exists'})