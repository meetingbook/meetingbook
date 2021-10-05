from tools.validation import email_validation, password_validation
from tools.func_for_psw import password_hashing
from domain.entities.admin import Admin

from tools.for_db.work_with_admin_info import add_admin


class AdminRegister:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def admin_register(self):
        checked_email = email_validation(self.email)
        checked_password = password_validation(self.password)
        hashed_password = password_hashing(checked_password)
        admin = Admin(checked_email, hashed_password)
        add_admin(admin)
