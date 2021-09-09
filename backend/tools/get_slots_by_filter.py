from db.models import Slots, SlotsShema


def get_slots_by_filter(filter):
    """Return list of slots with <filter>
    """
    if filter == "booking":
        booking_slots = Slots.query.filter(Slots.booking_id).all()
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(booking_slots)
        return output
    elif filter == "available":
        booking_slots = Slots.query.filter(Slots.booking_id.is_(None)).all()
        slots_shema = SlotsShema(many=True)
        output = slots_shema.dump(booking_slots)
        return output
