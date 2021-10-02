import base64
import pytest

from domain.value_objects.password import Password
import db.models as models
from tools.create_db_for_tests import create_test_app_with_db


@pytest.fixture(scope='module')
def app_for_test():
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()
    yield test_app
    models.AdminInfo.query.delete()


def test_login(app_for_test):
    log = 'admin'
    psw = 'Pyth0n'
    incorrect_psw = "Incorrect_psw"
    unauthorized_log = 'unknown_log'
    prepared_psw = Password(psw).get_hashed_password()
    test_admin = models.AdminInfo(email=log, psw=prepared_psw)
    models.db.session.add(test_admin)
    models.db.session.commit()
    valid_credentials = base64.b64encode(f'{log}:{psw}'.encode()).decode('utf-8')
    invalid_psw_credentials = base64.b64encode(f'{log}:{incorrect_psw}'.encode()).decode('utf-8')
    unauthorized_credentials = base64.b64encode(f'{unauthorized_log}:{psw}'.encode()).decode('utf-8')

    response1 = app_for_test.get("/login/", headers={'Authorization': 'Basic ' + valid_credentials})
    response2 = app_for_test.get("/login/")
    response3 = app_for_test.get("/login/", headers={'Authorization': 'Basic ' + invalid_psw_credentials})
    response4 = app_for_test.get("/login/", headers={'Authorization': 'Basic ' + unauthorized_credentials})

    assert response1.status == '200 OK'
    assert response2.status == '401 UNAUTHORIZED'
    assert response3.status == '401 UNAUTHORIZED'
    assert response4.status == '401 UNAUTHORIZED'
