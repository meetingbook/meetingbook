from flask import Blueprint, request, jsonify, redirect

from domain.use_cases.admin_usecases import AdminRegister

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def registration():
    email = request.form['email']
    psw = request.form['psw']
    psw2 = request.form['psw2']
    if psw != psw2:
        return jsonify({'error': 'Password mismatch'})
    AdminRegister(email, psw).admin_register()
    return redirect('/login/', code=401)
