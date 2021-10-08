import pytest
from flask import json

import db.models as models
from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_links import add_link
from tools.for_db.work_with_slots import add_slot


@pytest.fixture(scope='module')
def app_for_test():
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()
    yield test_app
    models.AdminInfo.query.delete()


def test_guest_calendar_post(app_for_test):
    start = '2021-10-07T15:00:56.273Z'
    end = '2021-10-07T16:00:56.273Z'
    link_id = '123456789a'
    admin_id = 1
    app_for_test.post('/registration', data=json.dumps(dict(email='my@mail.com', password='Passw0rd')),
                      content_type='application/json')
    add_slot(start, end, admin_id)
    add_link(link_id, admin_id)
    res1 = app_for_test.post(f'/calendar/{link_id}/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test@ma.c',
                                                  topic='Topic', start=start, end=end)),
                             content_type='application/json')
    res2 = app_for_test.post(f'/calendar/asdfga/bookings/',
                             data=json.dumps(dict(guest_name='Name', guest_email='test@ma.c',
                                                  topic='Topic', start=start, end=end)),
                             content_type='application/json')
    assert res1.status == '200 OK'
    assert res2.status == '401 UNAUTHORIZED'

