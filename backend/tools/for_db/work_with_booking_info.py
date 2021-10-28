import db.models as models
from flask import make_response
from tools.for_db.work_with_slots import get_id_slice_of_slot, update_booking_id_in_slot
from tools.generate_uid import generate_uid


class BookingSlotException(Exception):
    pass


def add_booking_info(booking_inf_name, booking_inf_email):
    try:
        booking_inf = models.BookingInfo(name=booking_inf_name, email=booking_inf_email)
        models.db.session.add(booking_inf)
        models.db.session.commit()
    except Exception as e:
        return make_response({
            "status": 500,
            "detail": f"{e}"
        }, 500)


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


def delete_booking_info(booking_id):
    try:
        models.db.session.delete(query_booking_info_by_id(booking_id))
        models.db.session.flush()
    except Exception:
        models.db.session.rollback()
        raise BookingSlotException('Unable to delete booking info')
