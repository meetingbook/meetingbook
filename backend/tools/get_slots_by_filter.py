from flask import make_response
from sqlalchemy import and_, or_
from db.models import Slots, SlotsShema


def get_slots_by_filter(filter, admin_id, start_dt=None):
    """Return list of slots with <filter>
    """
    if filter == "booking":
        booking_slots = Slots.query.filter(and_(Slots.booking_id, Slots.admin_id == admin_id)).all()
    elif filter == "available":
        booking_slots = Slots.query.filter(and_(Slots.booking_id.is_(None), Slots.admin_id == admin_id,
                                                or_(start_dt is None, Slots.end_interval > start_dt))).all()
    else:
        return make_response({
            "status": 400,
            "detail": "Invalid filter"
        }, 400)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(booking_slots)
    return output
