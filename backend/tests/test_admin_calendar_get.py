import base64
from flask import json

from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_links import add_link

admin_email = 'test@test.test'
admin_psw = 'testtest'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


def test_guest_calendar_post_200():
    app_for_test = create_test_app_with_db().test_client()
    link_id = '123456789a'
    admin_id = 1
    app_for_test.post('/registration', data=json.dumps(dict(email=admin_email, password=admin_psw)),
                      content_type='application/json')
    add_link(link_id, admin_id, valid_until='2021-10-20 16:57:43.000424')
    response = app_for_test.get('/calendars/', headers={'Authorization': 'Basic ' + valid_credentials})

    assert response.json == {'links': [{'id': 1, 'link_id': '123456789a', 'valid_until': '2021-10-20 16:57:43.000424'}]}
    assert response.status == '200 OK'


def test_guest_calendar_post_401():
    app_for_test = create_test_app_with_db().test_client()
    response = app_for_test.get('/calendars/')
    assert response.status == '401 UNAUTHORIZED'
