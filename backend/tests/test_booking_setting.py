import base64
from tools.create_db_for_tests import create_test_app_with_db
from tools.func_for_psw import password_hashing
from tools.get_booking_settings import get_booking_settings
from tools.for_db.work_with_admin_info import add_admin
from tools.for_db.work_with_booking_settings import add_booking_settings

admin_email = 'test@test.test'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')
admin_psw = password_hashing('testtest')


duration = {"msd": "testduration"}
start_time = {"msg": "teststart_time"}
json = [
    {
        "duration": {"msd": "testduration"},
        "start_time": {"msg": "teststart_time"}
    }
]


def test_get_booking_settings_notempty():
    create_test_app_with_db().test_client()
    add_admin(admin_email, admin_psw)
    add_booking_settings(duration, start_time, 1)
    booking_settings = get_booking_settings(admin_email)
    assert booking_settings == json


def test_status_200():
    with create_test_app_with_db().test_client() as con:
        add_admin(admin_email, admin_psw)
        add_booking_settings(duration, start_time, 1)
        response = con.get('/booking_settings', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'
    assert response.json == [{'duration': {'msd': 'testduration'}, 'start_time': {'msg': 'teststart_time'}}]
