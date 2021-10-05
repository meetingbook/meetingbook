from domain.entities.email import Email
from domain.entities.admin import Admin
from domain.value_objects.password import Password
from tools.for_db.work_with_admin_info import add_admin


class AdminRegister:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def admin_register(self):
        checked_email = Email(self.email)
        checked_password = Password(self.password)
        hashed_password = checked_password.get_hashed_password()
        admin = Admin(checked_email.get_value(), hashed_password)
        add_admin(admin)
