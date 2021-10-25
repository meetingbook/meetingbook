from datetime import datetime, timedelta
from server.calendars_post_for_admin import get_expiry_date
from flask import json

from tools.datetime_convertations import DateTime




def test_expiry_date_30():
    now = datetime.utcnow()
    dt_after_30_days = now + timedelta(days=30)
    assert get_expiry_date() == DateTime(dt_after_30_days).convert_to_iso()


def test_expiry_date_1_day():
    special_expiry_date = "2022-10-20T21:48:47.000Z"
    one_day = {'data': {'valid_until': special_expiry_date}}
    assert get_expiry_date(one_day) == special_expiry_date


def test_generate_calendar_link_without_valid_until(app_for_test, test_admin):
    test_admin.register_admin()
    response = app_for_test.post("/calendars",
                                 headers=test_admin.get_valid_header(),
                                 data=json.dumps(dict(valid_until="")),
                                 content_type='application/json')
    assert response.status == "200 OK"
    assert response.json["valid_until"] != ""
    assert response.json["id"] != ""


def test_generate_calendar_link_with_valid_until(app_for_test, test_admin):
    response = app_for_test.post('/calendars',
                                 headers=test_admin.get_valid_header(),
                                 data=json.dumps(dict(valid_until="2022-10-16T23:21:25.908Z")),
                                 content_type="application/json")
    assert response.status == '200 OK'
    assert response.json["valid_until"] != ""
    assert response.json["id"] != ""
