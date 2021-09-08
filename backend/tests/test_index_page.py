import pytest
import server as app
from flask import json
from server.index import msg_hello


@pytest.fixture(scope='module')
def response_get():
    with app.app.test_client() as con:
        resp = con.get('/')
        yield resp


def test_index_context(response_get):
    data = json.loads(response_get.data)
    assert msg_hello == data


def test_index(response_get):
    assert response_get.status_code == 200
