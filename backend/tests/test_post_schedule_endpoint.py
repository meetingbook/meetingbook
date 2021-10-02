import server as serv
from tools.create_db_for_tests import create_test_app_with_db
import db.models as models


def test_response_post_500():
    models.db.drop_all()
    with serv.app.test_client() as con:
        resp = con.post('/schedule/start=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 500
    assert resp.json == {'detail': 'Delete error', 'status': 500}


def test_response_post_200():
    create_test_app_with_db()
    with serv.app.test_client() as con:
        resp = con.post('/schedule/start=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 200
    assert resp.json == [{'booking_id': None,
                          'end_interval': '2022-15-14T13:00',
                          'id': 1,
                          'start_interval': '2022-10-13T11:00'}]


def test_response_post_404():
    with serv.app.test_client() as con:
        resp = con.post('/schedule/star=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 404
