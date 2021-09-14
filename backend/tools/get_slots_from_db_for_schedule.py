from db.models import Slots, SlotsShema
from sqlalchemy import and_, or_
from tools.transform_str_to_datetime_and_back import transform_string_to_datetime, transform_datetime_to_string
from datetime import timedelta


def get_slots_from_db_for_schedule(date, filter, days):
    """Return list of slots for the day: <date>
    """
    end_interval = transform_datetime_to_string(transform_string_to_datetime(date) + timedelta(days=days))
    if filter is not None:
        if filter == "booking":
            list_of_slots_in_day_by_filter = Slots.query.filter(
                and_(

                    or_(Slots.start_interval.between(date, end_interval),
                        Slots.end_interval.between(date, end_interval),
                        and_(Slots.start_interval <= date, Slots.end_interval >= end_interval)),
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
    else:
        list_of_slots_in_week = Slots.query.filter(or_(Slots.start_interval.between(date, end_interval),
                                                       Slots.end_interval.between(date, end_interval),
                                                       and_(Slots.start_interval <= date, Slots.end_interval >= end_interval))).all()
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(list_of_slots_in_week)
        return output
