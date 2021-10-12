from sqlalchemy import and_

from db.models import Slots, SlotsShema


def get_slots_by_filter(filter, admin_id):
    """Return list of slots with <filter>
    """
    if filter == "booking":
        booking_slots = Slots.query.filter(and_(Slots.booking_id, Slots.admin_id == admin_id)).all()
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(booking_slots)
        return output
    elif filter == "available":
        booking_slots = Slots.query.filter(and_(Slots.booking_id.is_(None), Slots.admin_id == admin_id)).all()
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(booking_slots)
        return output
