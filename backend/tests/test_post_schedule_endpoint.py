import base64
import server as app
from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_admin_info import add_admin
from tools.func_for_psw import password_hashing

admin_email = 'test@test.test'
admin_psw = 'testtest'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


def test_status_401():
    with app.app.test_client() as con:
        resp = con.post('/schedule/start=2022-15-13T11:00&end=2022-10-14T13:00')
    assert resp.status_code == 401


def test_response_post_200():
    create_test_app_with_db()
    add_admin(admin_email, password_hashing(admin_psw))
    with app.app.test_client() as con:
        resp = con.post('/schedule/start=2022-10-13T11:00&end=2022-10-14T13:00', headers={'Authorization': 'Basic ' + valid_credentials})
    assert resp.status_code == 200
    assert resp.json == {'booking_id': None,
                          'end_interval': '2022-10-14T13:00:00.000Z',
                          'id': 1,
                          'start_interval': '2022-10-13T11:00:00.000Z'}


def test_response_post_404():
    with app.app.test_client() as con:
        resp = con.post('/schedule/star=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 404


def test_status_400():
    with app.app.test_client() as con:
        resp = con.post('/schedule/start=2022-15-13T11:00&end=2022-10-14T13:00', headers={'Authorization': 'Basic ' + valid_credentials})
    assert resp.json == {'detail': "400 Bad Request", 'status': 400}
    assert resp.status_code == 400
