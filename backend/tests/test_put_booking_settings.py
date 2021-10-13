import base64
from tools.create_db_for_tests import create_test_app_with_db
from tools.func_for_psw import password_hashing
from tools.put_booking_settings import put_booking_settings
from flask import json
from tools.for_db.work_with_admin_info import add_admin
from tools.for_db.work_with_booking_settings import add_booking_settings

admin_email = 'test@test.test'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')
admin_psw = password_hashing('testtest')


def test_put_booking_settings():
    create_test_app_with_db().test_client()
    add_admin(admin_email, admin_psw)
    add_booking_settings({'test': 'test'}, {'test': 'test'}, 1)
    upd_booking_settings = put_booking_settings({'new_test': 'new_test'}, {'new_test': 'new_test'}, admin_email)
    assert upd_booking_settings.json == [{'duration': {'new_test': 'new_test'}, 'start_time': {'new_test': 'new_test'}}]


def test_status():
    with create_test_app_with_db().test_client() as con:
        add_admin(admin_email, admin_psw)
        add_booking_settings({'test': 'test'}, {'test': 'test'}, 1)
        response = con.put('/booking_settings', data=json.dumps(dict(duration={'allowed_values': [80, 35]}, start_time={
            'allowed_values': [25, 45]})), content_type='application/json')
        response_1 = con.put('/booking_settings', data=json.dumps(dict(duration={'allowed_values': [80, 35]}, start_time={
            'allowed_values': [25, 45]})), headers={'Authorization': 'Basic ' + valid_credentials}, content_type='application/json')
        response_2 = con.put('/booking_settings', data=json.dumps(dict(duration={'allowed_values': '[80, 35]'}, start_time={
            'allowed_values': '[25, 45]'})), headers={'Authorization': 'Basic ' + valid_credentials}, content_type='application/json')
    assert response.status == '401 UNAUTHORIZED'
    assert response_1.status == '200 OK'
    assert response_1.json == [{'duration': {'allowed_values': [80, 35]}, 'start_time': {'allowed_values': [25, 45]}}]
    assert response_2.status == '400 BAD REQUEST'
