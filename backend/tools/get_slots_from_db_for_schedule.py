from db.models import Slots, SlotsShema
from tools.transform_str_to_datetime_and_back import transform_string_to_datetime, transform_datetime_to_string
from datetime import timedelta
from tools.query_slots_with_filter import query_slots_with_filter
from tools.query_slots_no_filter import query_slots_no_filter


def get_slots_from_db_for_schedule(date, filter, days):
    """Return list of slots for the day: <date>
    """
    end_interval = transform_datetime_to_string(transform_string_to_datetime(date) + timedelta(days=days))
    if filter is None:
        list_of_slots = query_slots_no_filter(date, end_interval)
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(list_of_slots)
        return output
    elif filter == "booking":
        list_of_booking_slots = query_slots_with_filter(date, end_interval, Slots.booking_id)
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(list_of_booking_slots)
        return output
    elif filter == "available":
        list_of_available_slots = query_slots_with_filter(date, end_interval, Slots.booking_id.is_(None))
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(list_of_available_slots)
        return output
    else:
        mes = ("invalid filter parameter")
        return mes
