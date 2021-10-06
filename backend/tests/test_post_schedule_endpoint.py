import server as serv
from tools.create_db_for_tests import create_test_app_with_db
from tools.add_admin_for_test import add_admin_for_test, valid_credentials


def test_status_401():
    with serv.app.test_client() as con:
        resp = con.post('/schedule/start=2022-15-13T11:00&end=2022-10-14T13:00')
    assert resp.status_code == 401


def test_response_post_200():
    create_test_app_with_db()
    add_admin_for_test('test@test.test', 'testtest')
    with serv.app.test_client() as con:
        resp = con.post('/schedule/start=2022-10-13T11:00&end=2022-10-14T13:00', headers={'Authorization': 'Basic ' + valid_credentials})
    assert resp.status_code == 200
    assert resp.json == [{'booking_id': None,
                          'end_interval': '2022-10-14T13:00',
                          'id': 1,
                          'start_interval': '2022-10-13T11:00'}]


def test_response_post_404():
    with serv.app.test_client() as con:
        resp = con.post('/schedule/star=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 404


def test_status_400():
    with serv.app.test_client() as con:
        resp = con.post('/schedule/start=2022-15-13T11:00&end=2022-10-14T13:00', headers={'Authorization': 'Basic ' + valid_credentials})
    assert resp.data == b'400 Bad Request'
