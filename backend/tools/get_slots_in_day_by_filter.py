from db.models import Slots
from sqlalchemy import and_


def get_slots_in_day_by_filter(date, filter):
    """Return list of slots with <filter> in day <date>
    """
    if filter == "booking":
        list_of_slots_in_day_by_filter = Slots.query.filter(
            and_(
                Slots.booking_id,
                Slots.start_interval.startswith(date)
            )
        )
        return list_of_slots_in_day_by_filter
    elif filter == "available":
        list_of_slots_in_day_by_filter = Slots.query.filter(
            and_(
                Slots.booking_id.is_(None),
                Slots.start_interval.startswith(date)
            )
        )
        return list_of_slots_in_day_by_filter
