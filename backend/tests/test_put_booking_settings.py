import base64
from tools.create_db_for_tests import create_test_app_with_db
from tools.func_for_psw import password_hashing
from tools.get_booking_settings import get_booking_settings
from tools.put_booking_settings import put_booking_settings
import db.models as models
import server as app
from flask import json
from tools.for_db.work_with_admin_info import add_admin
admin_email = 'test@test.test'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')
admin_psw = password_hashing('testtest')


def test_put_booking_settings():
    create_test_app_with_db()
    add_admin(admin_email, admin_psw)
    old_booking_settings = models.BookingSettings(duration={'test': 'test'}, start_time={'test': 'test'}, admin_id=1)
    models.db.session.add(old_booking_settings)
    models.db.session.commit()
    upd_booking_settings = put_booking_settings({'new_test': 'new_test'}, {'new_test': 'new_test'}, admin_email)
    assert upd_booking_settings.json == [{'duration': {'new_test': 'new_test'}, 'start_time': {'new_test': 'new_test'}}]


def test_status_401():
    with app.app.test_client() as con:
        response = con.put('/booking_settings')
    assert response.status == '401 UNAUTHORIZED'


def test_status_200():
    with app.app.test_client() as con:
        response = con.put('/booking_settings', data=json.dumps(dict(duration={'allowed_values': '[80, 35]'}, start_time={
                           'allowed_values': '[25, 45]'})), headers={'Authorization': 'Basic ' + valid_credentials}, content_type='application/json')
    assert response.status == '200 OK'
    assert response.json == [{'duration': {'allowed_values': '[80, 35]'}, 'start_time': {'allowed_values': '[25, 45]'}}]
    models.db.drop_all()
