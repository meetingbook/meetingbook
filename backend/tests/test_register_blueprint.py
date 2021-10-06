import pytest

import db.models as models
from flask import json
from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_admin_info import get_psw_from_db
from tools.func_for_psw import check_psw


@pytest.fixture(scope='module')
def app_for_test():
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()
    yield test_app
    models.AdminInfo.query.delete()


def test_admin_register_response(app_for_test):
    correct_email = 'mail@.com'
    incorrect_email = 'mail@com'
    correct_password = 'Password'
    incorrect_password = 'psw'
    response1 = app_for_test.post('/registration', data=json.dumps(dict(email=correct_email, password=correct_password)),
                                  content_type='application/json')
    response2 = app_for_test.post('/registration', data=json.dumps(dict(email=correct_email, password=correct_password)),
                                  content_type='application/json')
    response3 = app_for_test.post('/registration', data=json.dumps(dict(email=correct_email)),
                                  content_type='application/json')
    response4 = app_for_test.post('/registration', data=json.dumps(dict(password=correct_password)),
                                  content_type='application/json')
    response5 = app_for_test.post('/registration')
    response6 = app_for_test.post('/registration', data=json.dumps(dict(email=incorrect_email, password=correct_password)),
                                  content_type='application/json')
    response7 = app_for_test.post('/registration', data=json.dumps(dict(email=correct_email, password=incorrect_password)),
                                  content_type='application/json')
    assert response1.status == '200 OK'
    assert response2.status == '409 CONFLICT'
    assert response3.status == '400 BAD REQUEST'
    assert response4.status == '400 BAD REQUEST'
    assert response5.status == '400 BAD REQUEST'
    assert response6.status == '400 BAD REQUEST'
    assert response7.status == '400 BAD REQUEST'


def test_admin_added_to_db(app_for_test):
    email = 'mail@.com'
    password = 'Password'
    psw_from_db = get_psw_from_db(email)

    assert check_psw(password, psw_from_db)
