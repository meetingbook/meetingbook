import pytest

from tools.create_db_for_tests import create_test_app_with_db, get_admin_id_for_test
from tools.get_slots_by_filter import get_slots_by_filter
from db import models


@pytest.fixture(scope='module')
def create_admin_id():
    create_test_app_with_db()
    yield get_admin_id_for_test()


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
    booking_inf = models.BookingInfo(name=booking_inf_name, email=booking_inf_email)
    models.db.session.add(booking_inf)
    models.db.session.commit()
    slots = models.Slots(start_interval=start_interval, end_interval=end_interval,
                         booking_id=booking_id, admin_id=create_admin_id)
    models.db.session.add(slots)
    models.db.session.commit()

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
    slots = models.Slots(start_interval=start_interval, end_interval=end_interval, admin_id=create_admin_id)
    models.db.session.add(slots)
    models.db.session.commit()
    booking_slots = get_slots_by_filter("available", create_admin_id)
    assert booking_slots == json
    models.Slots.query.delete()
