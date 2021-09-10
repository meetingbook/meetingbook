from tools.create_db_for_tests import create_test_app_with_db
from tools.get_slots_in_week_by_filter import get_slots_in_week_by_filter
import db.models as models


def test_get_slots_in_week_by_booking_empty():
    try: 
        models.Slots.query.delete()
    except:
        create_test_app_with_db()
    create_test_app_with_db()
    booking_slots = get_slots_in_week_by_filter("2021-03-02", "booking")
    assert booking_slots == []


def test_get_slots_in_week_by_booking():
    start_interval = "2021-02-03T10:00"
    end_interval = "2021-02-03T12:00"
    booking_id = "1"
    booking_inf_name = "test"
    booking_inf_email = "@test"
    json = [
        {
            "admin_id": None,
            "booking_id": 1,
            "start_interval": "2021-02-03T10:00",
            "id": 1,
            "end_interval": "2021-02-03T12:00"
        }
    ]
    booking_inf = models.BookingInfo(name=booking_inf_name, email=booking_inf_email)
    models.db.session.add(booking_inf)
    models.db.session.commit()
    slots = models.Slots(start_interval=start_interval, end_interval=end_interval, booking_id=booking_id)
    models.db.session.add(slots)
    models.db.session.commit()

    booking_slots = get_slots_in_week_by_filter("2021-02-03", "booking")
    assert booking_slots == json


def test_get_slots_in_week_by_available_empty():
    available_slots = get_slots_in_week_by_filter("2021-02-03", "available")
    assert available_slots == []


def test_get_slots_in_week_by_available():
    start_interval = "2021-02-03T13:00"
    end_interval = "2021-02-03T15:00"
    json = [
        {
            "admin_id": None,
            "booking_id": None,
            "start_interval": "2021-02-03T13:00",
            "end_interval": "2021-02-03T15:00",
            "id": 2
        }
    ]
    slots = models.Slots(start_interval=start_interval, end_interval=end_interval)
    models.db.session.add(slots)
    models.db.session.commit()
    booking_slots = get_slots_in_week_by_filter("2021-02-03", "available")
    assert booking_slots == json
