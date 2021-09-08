import base64
import server as app


def test_admin_login_failed():
    app.app.config['TESTING'] = True
    test_app = app.app.test_client()
    response = test_app.get("/admin")
    assert response.status == '401 UNAUTHORIZED'


def test_admin_login_success():
    app.app.config['TESTING'] = True
    test_app = app.app.test_client()
    valid_credentials = base64.b64encode(b'admin:Pyth0n').decode('utf-8')
    response = test_app.get("/admin", headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'
