from tools.get_slots_by_filter import get_slots_by_filter
from tools.for_db.work_with_slots import add_slot_and_get_id
from tools.for_db.work_with_booking_info import add_booking_info


def test_get_slots_by_booking_empty(test_admin):
    booking_slots = get_slots_by_filter("booking", test_admin.get_id())
    assert booking_slots == []


def test_get_slots_by_booking(test_admin):
    start_interval = "2021-02-03T10:00"
    end_interval = "2021-02-03T12:00"
    booking_id = "1"
    booking_inf_name = "test"
    booking_inf_email = "@test"
    json = [
        {
            "booking_id": 1,
            "start_interval": "2021-02-03T10:00",
            "id": 1,
            "end_interval": "2021-02-03T12:00"
        }
    ]
    add_booking_info(booking_inf_name, booking_inf_email)
    add_slot_and_get_id(start_interval, end_interval, test_admin.get_id(), booking_id)
    booking_slots = get_slots_by_filter("booking", test_admin.get_id())
    assert booking_slots == json


def test_get_slots_by_available_empty(test_admin):
    available_slots = get_slots_by_filter("available", test_admin.get_id())
    assert available_slots == []


def test_get_slots_by_available(test_admin):
    start_interval = "2021-02-03T13:00"
    end_interval = "2021-02-03T15:00"
    json = [
        {
            "booking_id": None,
            "start_interval": "2021-02-03T13:00",
            "end_interval": "2021-02-03T15:00",
            "id": 2
        }
    ]
    add_slot_and_get_id(start_interval, end_interval, test_admin.get_id())
    booking_slots = get_slots_by_filter("available", test_admin.get_id())
    assert booking_slots == json
