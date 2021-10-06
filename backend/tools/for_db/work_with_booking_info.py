import db.models as models


class BookingSlotException(Exception):
    pass


def booking_slot(name, email, topic, start_interval, end_interval, admin_id):
    try:
        booking_info = models.BookingInfo(name=name, email=email, topic=topic)
        models.db.session.add(booking_info)
        models.Slots.query.filter_by(start_interval=start_interval, end_interval=end_interval, admin_id=admin_id).\
            update(booking_id=booking_info.id)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise BookingSlotException
    finally:
        models.db.session.close()
