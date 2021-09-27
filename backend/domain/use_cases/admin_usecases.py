from flask import jsonify

from domain.entities.email import Email
from domain.entities.admin import Admin
from domain.value_objects.password import Password
from domain.repositories.admin_repository import AdminDbRepository


class AdminRegister:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def admin_register(self):
        try:
            checked_email = Email(self.email)
            checked_password = Password(self.password)
            hashed_password = checked_password.get_hashed_password()
            admin = Admin(checked_email, hashed_password)
            AdminDbRepository.add_admin(admin)
        except:
            return jsonify({'error': 'such user already exists'})
