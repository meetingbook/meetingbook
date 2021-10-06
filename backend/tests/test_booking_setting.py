import base64
from tools.create_db_for_tests import create_test_app_with_db
from tools.func_for_psw import password_hashing
from tools.get_booking_settings import get_booking_settings
import db.models as models
import server as app

admin_email = 'test@test.test'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')
admin_psw = password_hashing('testtest')

def test_get_booking_settings_is_empty():
    create_test_app_with_db()
    admin = models.AdminInfo(email=admin_email, psw=admin_psw)
    models.db.session.add(admin)
    models.db.session.commit()
    booking_settings = get_booking_settings(admin_email)
    assert booking_settings == []


def test_get_booking_settings_notempty():
    duration = {"msd": "testduration"}
    start_time = {"msg": "teststart_time"}
    json = [
        {
            "duration": {"msd": "testduration"},
            "start_time": {"msg": "teststart_time"}
        }
    ]
    settings = models.BookingSettings(duration=duration, start_time=start_time, admin_id=1)
    models.db.session.add(settings)
    models.db.session.commit()

    booking_settings = get_booking_settings(admin_email)
    assert booking_settings == json


def test_status_200():
    with app.app.test_client() as con:
        response = con.get('/booking_settings', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'


def test_response_json():
    with app.app.test_client() as con:
        response = con.get('/booking_settings', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.json == [{'duration': {'msd': 'testduration'}, 'start_time': {'msg': 'teststart_time'}}]
