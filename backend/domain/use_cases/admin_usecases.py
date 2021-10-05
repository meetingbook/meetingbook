from tools.validation import email_validation, password_validation
from tools.func_for_psw import password_hashing

from tools.for_db.work_with_admin_info import add_admin


class AdminRegister:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def admin_register(self):
        checked_email = email_validation(self.email)
        checked_password = password_validation(self.password)
        hashed_password = password_hashing(checked_password)
        add_admin(checked_email, hashed_password)
