import base64

from flask import json
from server import app
from db.models import db
from tools.for_db.work_with_admin_info import get_admin_id


def create_test_app_with_db():
    app.app_context().push()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.drop_all()
    db.create_all()
    return app


class AdminForTests:
    def __init__(self):
        self.email = 'correct@email.com'
        self.password = 'Password'

    def register_and_get_admin_id_for_test(self):
        with create_test_app_with_db().test_client() as con:
            con.post('/registration',
                     data=json.dumps(dict(email=self.email, password=self.password)),
                     content_type='application/json')
            return get_admin_id(self.email)

    def get_valid_header(self):
        valid_credentials = base64.b64encode(f'{self.email}:{self.password}'.encode()).decode('utf-8')
        return {'Authorization': 'Basic ' + valid_credentials}
