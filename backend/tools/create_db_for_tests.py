import base64

from server import app
from db.models import db
from tools.for_db.work_with_admin_info import get_admin_id, add_admin
from tools.func_for_psw import password_hashing


def create_test_app_with_db():
    app.app_context().push()
    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.drop_all()
    db.create_all()
    return app


class AdminForTests:
    def __init__(self):
        self.email = 'correct@email.com'
        self.password = 'Password'
        self.id = None

    def register_admin(self):
        add_admin(self.email, password_hashing(self.password))
        self.id = get_admin_id(self.email)

    def get_id(self):
        return self.id

    def get_valid_header(self):
        valid_credentials = base64.b64encode(f'{self.email}:{self.password}'.encode()).decode('utf-8')
        return {'Authorization': 'Basic ' + valid_credentials}
