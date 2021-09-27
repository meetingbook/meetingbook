import pytest

import db.models as models
from tools.create_db_for_tests import create_test_app_with_db


@pytest.fixture(scope='module')
def app_for_test():
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()
    yield test_app
    models.AdminInfo.query.delete()


def test_admin_register(app_for_test):
    email = 'mail@.com'
    password = 'Password'
    response = app_for_test.post('/register', data=dict(email=email, psw=password))
    assert response.status == '401 UNAUTHORIZED'
