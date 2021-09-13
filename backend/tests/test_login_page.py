import base64

from tools.func_for_psw import prepare_psw_for_db
import db.models as models
from tools.create_db_for_tests import create_test_app_with_db


def test_login_failed():

    # Arrange
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()

    # Act
    response = test_app.get("/login/")

    # Assert
    assert response.status == '401 UNAUTHORIZED'


def test_login_successful():

    # Arrange
    log = 'admin'
    psw = 'Pyth0n'
    prepared_psw = prepare_psw_for_db(psw)
    app_for_test = create_test_app_with_db()
    test_admin = models.AdminInfo(email=log, psw=prepared_psw)
    models.db.session.add(test_admin)
    models.db.session.commit()
    test_app = app_for_test.test_client()
    valid_credentials = base64.b64encode(f'{log}:{psw}'.encode()).decode('utf-8')

    # Act
    response = test_app.get("/login/", headers={'Authorization': 'Basic ' + valid_credentials})

    models.AdminInfo.query.delete()

    # Assert
    assert response.status == '200 OK'
