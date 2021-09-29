import db.models as models
from db.models import Slots, SlotsShema


def add_slot_from_db_for_schedule_admin(start, end):
    """Add new free slots in db for admin schedule.
    If the slot is added - return json with this slots.
    If the slot is don't added - return error msg
    """
    try:
        slots = models.Slots(start_interval=start, end_interval=end)
        models.db.session.add(slots)
        models.db.session.commit()
        return get_last_slot_id(slots.id)
    except Exception:
        models.db.session.rollback()
        return {
            'msg': "Don't added slot"
        }


def get_last_slot_id(slots_id):
    id_added_slots = Slots.query.filter(Slots.id == slots_id)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(id_added_slots)
    return output
