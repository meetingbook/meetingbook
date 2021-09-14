from db.models import Slots
from sqlalchemy import and_, or_


def query_slots_with_filter(date, end_interval, none_or_not):
    list_of_slots = Slots.query.filter(
        and_(
            or_(Slots.start_interval.between(date, end_interval),
                Slots.end_interval.between(date, end_interval),
                and_(Slots.start_interval <= date, Slots.end_interval >= end_interval)),
            none_or_not
        )
    )
    return list_of_slots
