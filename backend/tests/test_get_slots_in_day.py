import pytest

from tools.create_db_for_tests import create_test_app_with_db, get_admin_id_for_test
from tools.get_slots_from_db_for_schedule import get_slots_from_db_for_schedule
from db import models


@pytest.fixture(scope='module')
def create_admin_id():
    create_test_app_with_db()
    yield get_admin_id_for_test()


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
    booking_inf = models.BookingInfo(name=booking_inf_name, email=booking_inf_email)
    first_slots = models.Slots(start_interval=first_start_interval, end_interval=first_end_interval,
                               booking_id=booking_id, admin_id=create_admin_id)
    second_slots = models.Slots(start_interval=second_start_interval, end_interval=second_end_interval,
                                admin_id=create_admin_id)
    models.db.session.add(booking_inf)
    models.db.session.add(first_slots)
    models.db.session.add(second_slots)
    models.db.session.commit()

    booking_slots = get_slots_from_db_for_schedule(create_admin_id, "2021-02-03", filter=None, days=1)
    assert booking_slots == json
    models.Slots.query.delete()
