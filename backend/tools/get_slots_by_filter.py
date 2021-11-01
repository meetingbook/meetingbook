from sqlalchemy import and_, or_
from db.models import Slots, SlotsShema
from tools.build_response import build_response


def get_slots_by_filter(filter, admin_id, start_filter=None):
    """Return list of slots with <filter>
    """
    if filter == "booking":
        booking_slots = Slots.query.filter(and_(Slots.booking_id, Slots.admin_id == admin_id, )).all()
    elif filter == "available":
        booking_slots = Slots.query.filter(and_(Slots.booking_id.is_(None), Slots.admin_id == admin_id,
                                                or_(start_filter is None, start_filter))).all()

    else:
        return build_response("Invalid filter", 400)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(booking_slots)
    return output
