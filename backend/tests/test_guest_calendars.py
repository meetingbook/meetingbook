import pytest
from flask import json

from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_links import add_link
from tools.for_db.work_with_slots import add_slots


@pytest.fixture(scope='module')
def app_for_test():
    yield create_test_app_with_db().test_client()


start = '2021-10-07T15:00:56.273Z'
end = '2021-10-07T16:00:56.273Z'
link_id = '123456789a'
admin_id = 1


def test_guest_calendar_post(app_for_test):
    app_for_test.post('/registration', data=json.dumps(dict(email='my@mail.com', password='Passw0rd')),
                      content_type='application/json')
    add_slots(start, end, admin_id)
    add_link(link_id, admin_id, valid_until='2021-10-20 18:14:21.506393')
    res1 = app_for_test.post(f'/calendars/{link_id}/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test@ma.c',
                                                  topic='Topic', start=start, end=end)),
                             content_type='application/json')
    res2 = app_for_test.post('/calendars/asdfga/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test@ma.c',
                                                  topic='Topic', start=start, end=end)),
                             content_type='application/json')
    res3 = app_for_test.post(f'/calendars/{link_id}/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test@ma.c', start=start, end=end)),
                             content_type='application/json')
    res4 = app_for_test.post(f'/calendars/{link_id}/bookings/',
                             data=json.dumps(dict(guest_email='test@ma.c', start=start, end=end)),
                             content_type='application/json')
    res5 = app_for_test.post(f'/calendars/{link_id}/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test.c',
                                                  topic='Topic', start=start, end=end)),
                             content_type='application/json')
    assert res1.status == '200 OK'
    assert res2.status == '401 UNAUTHORIZED'
    assert res3.status == '409 CONFLICT'
    assert res4.status == '400 BAD REQUEST'
    assert res5.status == '400 BAD REQUEST'


def test_guest_calendar_get_200(app_for_test):
    res = app_for_test.get(f'/calendars/{link_id}')
    assert res.status == '200 OK'
    assert res.json == {'id': 1, 'slots': [], 'valid_until': '2021-10-20 18:14:21.506393'}


def test_guest_calendar_get_404(app_for_test):
    res = app_for_test.get('/calendars/link')
    assert res.status == '404 NOT FOUND'


def test_guest_calendar_get_401(app_for_test):
    add_link('abc', admin_id, valid_until='2021-10-10 18:14:21.506393')
    res = app_for_test.get('/calendars/abc')
    assert res.status == '401 UNAUTHORIZED'
