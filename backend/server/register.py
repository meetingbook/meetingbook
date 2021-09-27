from flask import Blueprint, request, redirect

from domain.use_cases.admin_usecases import AdminRegister

register_blueprint = Blueprint('register_blueprint', __name__)


@register_blueprint.route('/register', methods=['POST'])
def registration():
    email = request.form['email']
    psw = request.form['psw']
    AdminRegister(email, psw).admin_register()
    return redirect('/login/', code=401)
