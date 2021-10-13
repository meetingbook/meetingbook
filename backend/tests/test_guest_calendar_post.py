from flask import json

from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_links import add_link
from tools.for_db.work_with_slots import add_slots


def test_guest_calendar_post():
    app_for_test = create_test_app_with_db().test_client()
    start = '2021-10-07T15:00:56.273Z'
    end = '2021-10-07T16:00:56.273Z'
    link_id = '123456789a'
    admin_id = 1
    app_for_test.post('/registration', data=json.dumps(dict(email='my@mail.com', password='Passw0rd')),
                      content_type='application/json')
    add_slots(start, end, admin_id)
    add_link(link_id, admin_id)
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
