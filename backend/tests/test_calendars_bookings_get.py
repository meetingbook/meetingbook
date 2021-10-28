from tools.for_db.work_with_links import add_link
from tools.for_db.work_with_booking_info import add_booking_info_and_get_id, get_booking_info
from tools.for_db.work_with_slots import add_slots, get_slots_by_admin_id_and_booking_id

json = {
    'end': '2024-12-02T10:30:47.984Z',
    'guest_email': 'test@test.by',
    'guest_name': 'vasia',
    'start': '2024-12-02T10:00:47.984Z',
    'topic': 'testestest',
}


def test_calendar_booking_get(app_for_test, test_admin):
    add_slots('2024-12-02T10:00:47.984Z', '2024-12-02T10:30:47.984Z', test_admin.get_id())
    id = add_booking_info_and_get_id('2024-12-02T10:00:47.984Z', '2024-12-02T10:30:47.984Z',
                                     test_admin.get_id(), 'vasia', 'test@test.by', 'testestest')
    add_link('test', test_admin.get_id())
    add_link('testfail', test_admin.get_id(), "2020-10-14T13:41:23.936Z")

    result = get_slots_by_admin_id_and_booking_id(test_admin.get_id(), id)
    res_booking_info = get_booking_info(id)
    req_1 = app_for_test.get('/calendars/test/bookings/{}'.format(id))
    req_2 = app_for_test.get('/calendars/fail/bookings/{}'.format(id))
    req_3 = app_for_test.get('/calendars/test/bookings/5')
    req_4 = app_for_test.get('/calendars/testfail/bookings/2')

    assert result == ('2024-12-02T10:00:47.984Z', '2024-12-02T10:30:47.984Z')
    assert res_booking_info.name == 'vasia'
    assert req_1.json['end'] == '2024-12-02T10:30:47.984Z'
    assert req_1.json['guest_email'] == 'test@test.by'
    assert req_1.json['uuid'] != {}
    assert req_2.json == {'detail': 'Shareable link not found', 'status': 404}
    assert req_3.json == {'detail': 'Booking not found', 'status': 404}
    assert req_4.json == {'detail': 'Unauthorized - link has expired', 'status': 401}
