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


def get_admin_id_for_test():
    correct_email = 'correct@email.com'
    with create_test_app_with_db().test_client() as con:
        con.post('/registration',
                 data=json.dumps(dict(email=correct_email, password='Correct_password')),
                 content_type='application/json')
        return get_admin_id(correct_email)
