import pytest
import base64
import server.app as app
from flask import json



@pytest.fixture(scope='module')
def response_get():
    with app.app.test_client() as con:
        resp = con.get('/')
        yield resp


def test_index_context(response_get):
    data = json.loads(response_get.data)
    assert app.msg_hello == data


def test_index(response_get):
    assert response_get.status_code == 200


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
