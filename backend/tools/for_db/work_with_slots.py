from sqlalchemy import and_, or_
from db import models
from db.models import Slots, SlotsShema


class DbSlotException(Exception):
    pass


def add_slot_and_get_id(start_interval, end_interval, admin_id, booking_id=None):
    try:
        slots = models.Slots(start_interval=start_interval, end_interval=end_interval,
                             booking_id=booking_id, admin_id=admin_id)
        models.db.session.add(slots)
        models.db.session.commit()
        return slots.id
    except Exception:
        models.db.session.rollback()
        raise DbSlotException('Error. Unable to add slot')
    finally:
        models.db.session.close()


def get_id_slice_of_slot(start, end, admin_id):     # takes a slice of a slot and cuts it out of the larger from db
    try:
        slot_from_db = Slots.query.filter(      # search for a slot in the database
            and_(Slots.admin_id == admin_id,
                 Slots.start_interval <= start,
                 Slots.end_interval >= end)).first()
        if slot_from_db.booking_id is not None:     # only shares unbooked slots
            raise DbSlotException('Error. Slot already booked')
        start_db = slot_from_db.start_interval
        end_db = slot_from_db.end_interval
        if start_db == start and end_db == end:     # if slice == slot from db
            return slot_from_db.id
        models.db.session.delete(slot_from_db)      # delete slot from db
        if start_db < start:        # if start_interval from db is less then start_interval slice
            slot1 = Slots(start_interval=start_db, end_interval=start, admin_id=admin_id)
            models.db.session.add(slot1)    # add interval less then slice
        if end_db > end:            # if end_interval from db is greater than end_interval slice
            slot3 = Slots(start_interval=end, end_interval=end_db, admin_id=admin_id)
            models.db.session.add(slot3)    # add interval greater then slice
        slot2 = Slots(start_interval=start, end_interval=end, admin_id=admin_id)    # add slice
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


def canceling_booking_id_from_slot(booking_id):
    try:
        Slots.query.filter_by(booking_id=booking_id).update({Slots.booking_id: None}, synchronize_session=False)
        models.db.session.flush()
    except Exception:
        models.db.session.rollback()
        raise DbSlotException('Error. Unable to cancel booking id from slot')


def get_slot_by_id(slots_id):
    id_added_slots = Slots.query.filter_by(id=slots_id).first()
    slots_shema = SlotsShema(many=False)
    output = slots_shema.dump(id_added_slots)
    return output


def query_slots(admin_id, date, end_interval, none_or_not=None):
    list_of_slots = Slots.query.filter(
        and_(
            or_(Slots.start_interval.between(date, end_interval),
                Slots.end_interval.between(date, end_interval),
                and_(Slots.start_interval <= date, Slots.end_interval >= end_interval)),
            or_(none_or_not is None,
                none_or_not),
            Slots.admin_id == admin_id
        )
    )
    return list_of_slots


def marshmallow_for_query_slots(qury_slots):
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(qury_slots.all())
    return output
