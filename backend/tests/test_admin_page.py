import base64
import server as app


def test_admin_login_failed():
    with app.app.test_client() as con:
        response = con.get("/admin")
    assert response.status == '401 UNAUTHORIZED'


def test_admin_login_success():
    app.app.config['TESTING'] = True
    with app.app.test_client() as con:
        valid_credentials = base64.b64encode(b'admin:Pyth0n').decode('utf-8')
        response = con.get("/admin", headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'
