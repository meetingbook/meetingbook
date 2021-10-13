import db.models as models
from flask import make_response
from tools.for_db.work_with_slots import get_id_slice_of_slot, update_booking_id_in_slot


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


def add_booking_info_and_get_id(start, end, admin_id, name, email, topic=None):
    try:
        booking_info = models.BookingInfo(name=name, email=email, topic=topic)
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
    return booking_id


def delete_booking_info(booking_id):
    try:
        booking_info = models.BookingInfo.query.filter_by(id=booking_id)
        models.db.session.delete(booking_info)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise BookingSlotException('Unable to delete booking info')

    finally:
        models.db.session.close()
