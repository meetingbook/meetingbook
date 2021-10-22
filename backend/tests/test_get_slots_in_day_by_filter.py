from tools.get_slots_from_db_for_schedule import get_slots_from_db_for_schedule
from tools.for_db.work_with_slots import add_slot_and_get_id
from tools.for_db.work_with_booking_info import add_booking_info


def test_get_slots_in_day_by_booking_empty(test_admin):
    booking_slots = get_slots_from_db_for_schedule(test_admin.get_id(), "2021-03-02", "booking", 1)
    assert booking_slots == []


def test_get_slots_in_day_by_booking(test_admin):
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
    booking_slots = get_slots_from_db_for_schedule(test_admin.get_id(), "2021-02-03", "booking", 1)
    assert booking_slots == json


def test_get_slots_in_day_by_available_empty(create_admin_id):
    available_slots = get_slots_from_db_for_schedule(create_admin_id, "2021-02-03", "available", 1)
    assert available_slots == []


def test_get_slots_in_day_by_available(create_admin_id):
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
    add_slot_and_get_id(start_interval, end_interval, create_admin_id)
    booking_slots = get_slots_from_db_for_schedule(create_admin_id, "2021-02-03", "available", 1)
    assert booking_slots == json
