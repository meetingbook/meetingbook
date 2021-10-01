from domain.entities.email import Email
from domain.entities.admin import Admin
from domain.value_objects.password import Password
from domain.repositories.admin_repository import AdminDbRepository


class UseCase:
    def exec():
        raise Exception("Implement exec() method")


class AdminRegister(UseCase):

    def __init__(self, repo: AdminDbRepository):
        self.repo = repo

    def exec(self, email, password):
        checked_email = Email(email)
        checked_password = Password(password)
        hashed_password = checked_password.get_hashed_password()
        admin = Admin(checked_email.get_value(), hashed_password)
        repo.add_admin(admin)
