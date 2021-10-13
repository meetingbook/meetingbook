import pytest
from tools.create_db_for_tests import create_test_app_with_db
from tools.get_slots_from_db_for_schedule import get_slots_from_db_for_schedule
from tools.for_db.work_with_slots import add_slots
from tools.for_db.work_with_booking_info import add_booking_info


@pytest.fixture(scope='module')
def create_admin_id(test_admin):
    create_test_app_with_db()
    yield test_admin.register_and_get_admin_id_for_test()


def test_get_slots_in_day_empty(create_admin_id):
    slots = get_slots_from_db_for_schedule(create_admin_id, "2021-03-02", filter=None, days=1)
    assert slots == []


def test_get_slots_in_day(create_admin_id):
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
    add_slots(first_start_interval, first_end_interval, create_admin_id, booking_id)
    add_slots(second_start_interval, second_end_interval, create_admin_id)

    booking_slots = get_slots_from_db_for_schedule(create_admin_id, "2021-02-03", filter=None, days=1)
    assert booking_slots == json
