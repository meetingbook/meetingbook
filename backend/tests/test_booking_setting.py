from tools.create_db_for_tests import create_test_app_with_db
from tools.get_booking_settings import get_booking_settings
import db.models as models
import server as app


def test_get_booking_settings_is_empty():
    create_test_app_with_db()
    booking_settings = get_booking_settings()
    assert booking_settings == []


def test_get_booking_settings_notempty():
    admin_email = 'test@test.test'
    admin_psw = 'testtest'
    duration = {"msd": "testduration"}
    start_time = {"msg": "teststart_time"}
    json = [
        {
            "duration": {"msd": "testduration"},
            "start_time": {"msg": "teststart_time"}
        }
    ]
    admin = models.AdminInfo(email=admin_email, psw=admin_psw)
    models.db.session.add(admin)
    models.db.session.commit()
    settings = models.BookingSettings(duration=duration, start_time=start_time, admin_id=1)
    models.db.session.add(settings)
    models.db.session.commit()

    booking_settings = get_booking_settings()
    assert booking_settings == json


def test_status_200():
    with app.app.test_client() as con:
        response = con.get('/booking_settings')
    assert response.status == '200 OK'


def test_response_json():
    with app.app.test_client() as con:
        response = con.get('/booking_settings')
    assert response.json == [{'duration': {'msd': 'testduration'}, 'start_time': {'msg': 'teststart_time'}}]


def test_status_500():
    models.db.drop_all()
    booking_settings = get_booking_settings()
    assert booking_settings == {'detail': 'DB not found', 'status': 500}
