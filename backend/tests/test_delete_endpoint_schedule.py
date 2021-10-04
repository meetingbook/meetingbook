import server as app
from tools.create_db_for_tests import create_test_app_with_db


def test_response_delete():
    create_test_app_with_db()
    with app.app.test_client() as con:
        resp = con.delete('/schedule/interval_id=1')
    assert resp.json == {'detail': 'Delete error', 'status': 500}
