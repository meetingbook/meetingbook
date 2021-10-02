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
    correct_email = 'mail@.com'
    incorrect_email = 'mail@com'
    correct_password = 'Password'
    incorrect_password = 'psw'
    response1 = app_for_test.post('/register', data=dict(email=correct_email, password=correct_password))
    response2 = app_for_test.post('/register', data=dict(email=correct_email, password=correct_password))
    response3 = app_for_test.post('/register', data=dict(email=correct_email))
    response4 = app_for_test.post('/register', data=dict(password=correct_password))
    response5 = app_for_test.post('/register')
    response6 = app_for_test.post('/register', data=dict(email=incorrect_email, password=correct_password))
    response7 = app_for_test.post('/register', data=dict(email=correct_email, password=incorrect_password))
    assert response1.status == '200 OK'
    assert response2.status == '409 CONFLICT'
    assert response3.status == '400 BAD REQUEST'
    assert response4.status == '400 BAD REQUEST'
    assert response5.status == '400 BAD REQUEST'
    assert response6.status == '400 BAD REQUEST'
    assert response7.status == '400 BAD REQUEST'
