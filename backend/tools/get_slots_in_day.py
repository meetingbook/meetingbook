from db.models import Slots, SlotsShema


def get_slots_in_day(date):
    """Return list of slots for the day: <date>
    """
    list_of_slots_in_day = Slots.query.filter(Slots.start_interval.startswith(date)).all()
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(list_of_slots_in_day)
    return output
