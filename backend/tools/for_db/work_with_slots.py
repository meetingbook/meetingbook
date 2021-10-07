from sqlalchemy import and_

from db import models
from db.models import Slots


class SplitSlotException(Exception):
    pass


class BookingSlotException(Exception):
    pass


def get_id_slice_of_slot(start, end, admin_id):
    try:
        slot_from_db = Slots.query.filter(
            and_(Slots.admin_id == admin_id,
                 Slots.start_interval <= start,
                 Slots.end_interval >= end)).first()
        start_db = slot_from_db.start_interval
        end_db = slot_from_db.end_interval
        slot_from_db.delete()
        if start_db < start:
            slot1 = Slots(start_interval=start_db, end_interval=start)
            models.db.session.add(slot1)
        if end_db > end:
            slot3 = Slots(start_interval=end, end_interval=end_db, admin_id=admin_id)
            models.db.session.add(slot3)
        slot2 = Slots(start_inteval=start, end_interval=end, admin_id=admin_id)
        models.db.session.add(slot2)
        slot_id = slot2.id
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise SplitSlotException('Error. Unable to split slot')
    finally:
        models.db.session.close()
    return slot_id


def update_booking_id_in_slot(slot_id, booking_id):
    try:
        Slots.query.filter_by(id=slot_id).update(booking_id=booking_id)
    except Exception:
        raise BookingSlotException('Error. Unable to book slot')
    finally:
        models.db.session.close()
