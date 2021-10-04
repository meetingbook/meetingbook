from db.models import Slots, SlotsShema
from tools.transform_str_to_datetime_and_back import transform_string_to_datetime, transform_datetime_to_string
from datetime import timedelta
from tools.query_slots import query_slots
from flask import make_response


def get_slots_from_db_for_schedule(date, filter, days):
    """Return list of slots for the day: <date>
    """
    end_interval = transform_datetime_to_string(transform_string_to_datetime(date) + timedelta(days=days))
    if filter is None:
        list_of_slots = query_slots(date, end_interval)
    elif filter == "booking":
        list_of_slots = query_slots(date, end_interval, Slots.booking_id)
    elif filter == "available":
        list_of_slots = query_slots(date, end_interval, Slots.booking_id.is_(None))
    else:
        return make_response({
            "status": 400,
            "detail": "Invalid filter"
        }, 400)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(list_of_slots)
    return output
