from db.models import Slots, SlotsShema
from sqlalchemy import and_
from tools.transform_str_to_datetime_and_back import transform_string_to_datetime, transform_datetime_to_string
from datetime import timedelta


def get_slots_in_week_by_filter(date, filter):
    """Return list of slots for the day: <date>
    """
    end_interval = transform_datetime_to_string(transform_string_to_datetime(date) + timedelta(days=7))
    if filter == "booking":
        list_of_slots_in_day_by_filter = Slots.query.filter(
            and_(
                Slots.start_interval.between(date, end_interval),
                Slots.booking_id
            )
        )
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(list_of_slots_in_day_by_filter)
        return output
    elif filter == "available":
        list_of_slots_in_day_by_filter = Slots.query.filter(
            and_(
                Slots.start_interval.between(date, end_interval),
                Slots.booking_id.is_(None)
            )
        )
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(list_of_slots_in_day_by_filter)
        return output
