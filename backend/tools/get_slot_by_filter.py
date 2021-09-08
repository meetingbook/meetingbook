from db.models import Slots


def get_slot_by_filter(filter):
    """Return list of slots with <filter>
    """
    if filter == "booking":
        booking_slots = Slots.query.filter(Slots.booking_id).all()
        return booking_slots
    elif filter == "available":
        booking_slots = Slots.query.filter(Slots.booking_id.is_(None)).all()
        return booking_slots
