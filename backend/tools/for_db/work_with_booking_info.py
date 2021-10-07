import db.models as models


class BookingSlotException(Exception):
    pass


def add_booking_info_and_get_id(name, email, topic):
    try:
        booking_info = models.BookingInfo(name=name, email=email, topic=topic)
        models.db.session.add(booking_info)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise BookingSlotException
    finally:
        models.db.session.close()
    return booking_info.id
