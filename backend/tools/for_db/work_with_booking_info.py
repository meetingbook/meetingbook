from tools.generate_uid import generate_uid
from tools.build_response import build_response
from tools.for_db.work_with_slots import BookingNotFound
import db.models as models
from tools.for_db.work_with_slots import get_id_slice_of_slot, update_booking_id_in_slot


class BookingSlotException(Exception):
    pass


def add_booking_info(booking_inf_name, booking_inf_email):
    try:
        booking_inf = models.BookingInfo(name=booking_inf_name, email=booking_inf_email)
        models.db.session.add(booking_inf)
        models.db.session.commit()
    except Exception as e:
        return build_response(f"{e}", 500)


def add_booking_info_and_get_uuid(start, end, admin_id, name, email, topic=None):
    try:
        uuid = generate_uid()
        booking_info = models.BookingInfo(name=name, email=email, topic=topic, uuid=uuid)
        models.db.session.add(booking_info)
        slot_id = get_id_slice_of_slot(start, end, admin_id)
        booking_id = booking_info.id
        update_booking_id_in_slot(slot_id, booking_id)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise BookingSlotException('error adding booking info')
    finally:
        models.db.session.close()
    return uuid


def query_booking_info_by_id(booking_id):
    return models.BookingInfo.query.filter_by(id=booking_id).first()


def query_booking_info_by_uuid(uuid):
    return models.BookingInfo.query.filter_by(uuid=uuid).first()


def delete_booking_info_and_get_id(uuid):
    try:
        booking_info = query_booking_info_by_uuid(uuid)
        booking_id = booking_info.id
        models.db.session.delete(booking_info)
        models.db.session.flush()
    except Exception:
        models.db.session.rollback()
        raise BookingSlotException('Unable to delete booking info')
    return booking_id


def get_booking_info(booking_id):
    booking_info = models.BookingInfo.query.filter_by(id=booking_id).first()
    if booking_info is None:
        raise BookingNotFound('Booking not found')
    return booking_info
