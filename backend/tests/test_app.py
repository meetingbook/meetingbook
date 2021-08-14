import pytest
from flask import Flask, json, jsonify
import server.app as ap


@pytest.fixture(scope='module')
def response_get():
    with ap.app.test_client() as con:
        resp = con.get('/')
        yield resp


def test_index_context(response_get):
    data = json.loads(response_get.data)
    assert ap.msg_hello == data

def test_index(response_get):
    assert response_get.status_code == 200