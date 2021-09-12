import base64

from tools.func_for_psw import prepare_psw_for_db
import db.models as models
from tools.create_db_for_tests import create_test_app_with_db


def test_login_failed():
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()
    response = test_app.get("/login/")
    assert response.status == '401 UNAUTHORIZED'


def test_login_successful():
    log = 'admin'
    psw = 'Pyth0n'
    prepared_psw = prepare_psw_for_db(psw)
    app_for_test = create_test_app_with_db()
    test_admin = models.AdminInfo(email=log, psw=prepared_psw)
    models.db.session.add(test_admin)
    models.db.session.commit()
    test_app = app_for_test.test_client()
    valid_credentials = base64.b64encode(f'{log}:{psw}'.encode()).decode('utf-8')
    response = test_app.get("/login/", headers={'Authorization': 'Basic ' + valid_credentials})
    models.AdminInfo.query.delete()
    assert response.status == '200 OK'
