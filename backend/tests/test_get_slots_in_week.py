from tools.get_slots_from_db_for_schedule import get_slots_from_db_for_schedule
from tools.for_db.work_with_slots import add_slot_and_get_id
from tools.for_db.work_with_booking_info import add_booking_info


def test_get_slots_in_week_empty(test_admin):
    slots = get_slots_from_db_for_schedule(test_admin.get_id(), "2021-03-02", filter=None, days=7)
    assert slots == []


def test_get_slots_in_week(test_admin):
    first_start_interval = "2021-02-03T10:00"
    first_end_interval = "2021-02-03T12:00"
    second_start_interval = "2021-02-03T13:00"
    second_end_interval = "2021-02-03T15:00"
    booking_id = "1"
    booking_inf_name = "test"
    booking_inf_email = "@test"
    json = [
        {
            "booking_id": 1,
            "start_interval": "2021-02-03T10:00",
            "id": 1,
            "end_interval": "2021-02-03T12:00"
        },
        {
            "booking_id": None,
            "start_interval": "2021-02-03T13:00",
            "id": 2,
            "end_interval": "2021-02-03T15:00"
        }
    ]
    add_booking_info(booking_inf_name, booking_inf_email)
    add_slot_and_get_id(first_start_interval, first_end_interval, test_admin.get_id(), booking_id)
    add_slot_and_get_id(second_start_interval, second_end_interval, test_admin.get_id())

    booking_slots = get_slots_from_db_for_schedule(test_admin.get_id(), "2021-02-03", filter=None, days=7)
    assert booking_slots == json
