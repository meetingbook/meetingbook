from domain.entities.admin import Admin
from domain.repositories.admin_repository import AdminDbRepository
from domain.use_cases.work_with_password import WorkWithPassword
from flask import jsonify


class AdminRegister(Admin):
    def admin_register(self):
        try:
            password = self.get_password()
            hashed_password = WorkWithPassword.prepare_psw_for_db(password)
            AdminDbRepository.add_admin(self.get_mail(), hashed_password)
        except Exception:
            return jsonify({'error': 'such user already exists'})
