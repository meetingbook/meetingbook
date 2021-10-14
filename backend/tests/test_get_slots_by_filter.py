import pytest
from tools.create_db_for_tests import create_test_app_with_db
from tools.get_slots_by_filter import get_slots_by_filter
from tools.for_db.work_with_slots import add_slots
from tools.for_db.work_with_booking_info import add_booking_info


@pytest.fixture(scope='module')
def create_admin_id(test_admin):
    create_test_app_with_db()
    test_admin.register_admin()
    yield test_admin.get_id()


def test_get_slots_by_booking_empty(create_admin_id):
    booking_slots = get_slots_by_filter("booking", create_admin_id)
    assert booking_slots == []


def test_get_slots_by_booking(create_admin_id):
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
    add_slots(start_interval, end_interval, create_admin_id, booking_id)
    booking_slots = get_slots_by_filter("booking", create_admin_id)
    assert booking_slots == json


def test_get_slots_by_available_empty(create_admin_id):
    available_slots = get_slots_by_filter("available", create_admin_id)
    assert available_slots == []


def test_get_slots_by_available(create_admin_id):
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
    add_slots(start_interval, end_interval, create_admin_id)
    booking_slots = get_slots_by_filter("available", create_admin_id)
    assert booking_slots == json
