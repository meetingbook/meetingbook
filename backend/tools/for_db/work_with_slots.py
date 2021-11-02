from sqlalchemy import and_
from db import models
from db.models import Slots


class DbSlotException(Exception):
    pass


class BookingNotFound(Exception):
    pass


def add_slots(start_interval, end_interval, create_admin_id, booking_id=None):
    try:
        slots = models.Slots(start_interval=start_interval, end_interval=end_interval,
                             booking_id=booking_id, admin_id=create_admin_id)
        models.db.session.add(slots)
        models.db.session.commit()
        return slots.id
    except Exception:
        models.db.session.rollback()
        raise DbSlotException('Error. Unable to add slot')
    finally:
        models.db.session.close()


def get_id_slice_of_slot(start, end, admin_id):
    try:
        slot_from_db = Slots.query.filter(
            and_(Slots.admin_id == admin_id,
                 Slots.start_interval <= start,
                 Slots.end_interval >= end)).first()
        if slot_from_db.booking_id is not None:
            raise DbSlotException('Error. Slot already booked')
        start_db = slot_from_db.start_interval
        end_db = slot_from_db.end_interval
        if start_db == start and end_db == end:
            return slot_from_db.id
        models.db.session.delete(slot_from_db)
        if start_db < start:
            slot1 = Slots(start_interval=start_db, end_interval=start, admin_id=admin_id)
            models.db.session.add(slot1)
        if end_db > end:
            slot3 = Slots(start_interval=end, end_interval=end_db, admin_id=admin_id)
            models.db.session.add(slot3)
        slot2 = Slots(start_interval=start, end_interval=end, admin_id=admin_id)
        models.db.session.add(slot2)
        models.db.session.commit()
        slot_id = slot2.id
    except Exception:
        models.db.session.rollback()
        raise DbSlotException('Error. Unable to split slot')
    return slot_id


def update_booking_id_in_slot(slot_id, book_id):
    try:
        slot = Slots.query.filter_by(id=slot_id)
        if slot.first().booking_id is None:
            slot.update({Slots.booking_id: book_id}, synchronize_session=False)
            models.db.session.commit()
        else:
            raise DbSlotException
    except Exception:
        models.db.session.rollback()
        raise DbSlotException('Error. Unable to book slot')


def get_slots_by_admin_id_and_booking_id(id_admin, id_booking):
    slots = Slots.query.with_entities(
        Slots.start_interval,
        Slots.end_interval).filter_by(admin_id=id_admin, booking_id=id_booking).first()
    if slots is None:
        raise BookingNotFound('Booking not found')

    return slots
