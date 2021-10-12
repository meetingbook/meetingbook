import base64
from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_admin_info import add_admin
from tools.func_for_psw import password_hashing

admin_email = 'test@test.test'
admin_psw = 'testtest'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


def test_response_delete():
    with create_test_app_with_db().test_client() as con:
        add_admin(admin_email, password_hashing(admin_psw))
        resp = con.delete('/schedule/interval_id=1', headers={'Authorization': 'Basic ' + valid_credentials})
    assert resp.json == {'detail': 'Delete error', 'status': 500}
