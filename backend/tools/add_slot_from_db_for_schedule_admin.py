import db.models as models
from db.models import Slots, SlotsShema


def add_slot_from_db_for_schedule_admin(start, end):
    """Add new free slots in db for admin schedule
    """
    try:
        slots = models.Slots(start_interval=start, end_interval=end)
        models.db.session.add(slots)
        models.db.session.commit()
        return get_last_slot_id()
    except Exception:
        models.db.session.rollback()
        return 1


def get_last_slot_id():
    id = Slots.query.order_by(Slots.id.desc()).limit(1)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(id)
    return output
