import re
from flask import json

from tools.datetime_convertations import DateTime
from tools.for_db.work_with_booking_info import query_booking_info_by_id
from tools.for_db.work_with_links import add_link
from tools.for_db.work_with_slots import add_slot_and_get_id


start = '2021-10-07T15:00:56.273Z'
end = '2021-10-07T16:00:56.273Z'
dt_for_link = DateTime().utc_plus_delta(days=7)
end_interval = DateTime().utc_plus_delta(days=10)


def test_guest_calendar_post(app_for_test, test_admin, link_id):
    admin_id = test_admin.get_id()
    add_slot_and_get_id(start, end, admin_id)
    add_slot_and_get_id('2020-09-01T15:00:56.273Z', '2020-09-01T16:00:56.273Z', admin_id)
    add_slot_and_get_id(dt_for_link, end_interval, admin_id)
    add_link(link_id, admin_id, dt_for_link)
    res0 = app_for_test.post(f'/calendars/{link_id}/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test@ma.c',
                                                  topic='Topic', start=start, end='2021-10-07T15:30:56.273Z')),
                             content_type='application/json')
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
    assert res0.status == '409 CONFLICT'    # does not match with booking_settings
    assert res1.status == '200 OK'
    assert re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', res1.json['uuid'])
    assert res1.json['start'] == start
    assert res1.json['end'] == end
    assert res2.status == '401 UNAUTHORIZED'
    assert res3.status == '409 CONFLICT'
    assert res4.status == '400 BAD REQUEST'
    assert res5.status == '400 BAD REQUEST'


def test_guest_calendar_get_200(app_for_test, link_id):
    res = app_for_test.get(f'/calendars/{link_id}')
    assert res.status == '200 OK'
    assert res.json == {'id': 1, 'slots': [{'id': 3, 'start_interval': dt_for_link, 'end_interval': end_interval,
                                            'booking_id': None}], 'valid_until': dt_for_link}


def test_guest_calendar_get_404(app_for_test):
    res = app_for_test.get('/calendars/link')
    assert res.status == '404 NOT FOUND'


def test_guest_calendar_get_401(app_for_test, test_admin):
    add_link('abc', test_admin.get_id(), valid_until='2021-10-12T17:34:59.603Z')
    res = app_for_test.get('/calendars/abc')
    assert res.status == '401 UNAUTHORIZED'


def test_guest_calendar_delete_200(app_for_test, link_id):
    booking_uuid = query_booking_info_by_id(1).uuid
    res = app_for_test.delete(f'/calendars/{link_id}/bookings/{booking_uuid}')
    assert res.status == '200 OK'
    assert res.json == {'detail': 'Successful request', 'status': 200}


def test_guest_calendar_delete_409(app_for_test, link_id):
    res = app_for_test.delete(f'/calendars/{link_id}/bookings/1')
    assert res.status == '409 CONFLICT'
    assert res.json == {'detail': 'Unable to delete booking info', 'status': 409}


def test_guest_calendar_delete_404(app_for_test):
    res = app_for_test.delete('/calendars/wrong_link/bookings/1')
    assert res.status == '404 NOT FOUND'
    assert res.json == {'detail': 'Shareable link not found', 'status': 404}


def test_guest_calendar_delete_401(test_admin, app_for_test, link_id):
    add_link('expired_link', test_admin.get_id(), DateTime().utc_plus_delta(days=-1))
    res = app_for_test.delete('/calendars/expired_link/bookings/1')
    assert res.status == '401 UNAUTHORIZED'
    assert res.json == {'detail': 'Unauthorized - link has expired', 'status': 401}
