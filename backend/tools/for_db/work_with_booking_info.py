import db.models as models


class BookingSlotException(Exception):
    pass


def add_booking_info_and_get_id(name, email, topic=None):
    try:
        booking_info = models.BookingInfo(name=name, email=email, topic=topic)
        models.db.session.add(booking_info)
        models.db.session.commit()
        booking_id = booking_info.id
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
    except:
        models.db.session.rollback()
    finally:
        models.db.session.close()
