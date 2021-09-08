from db.models import Slots


def get_slot_in_day(date):
    """Return list of slots for the day: <date>
    """
    list_of_slots_in_day = Slots.query.filter(Slots.start_interval.startswith(date)).all()
    return list_of_slots_in_day
