import db.models as models


class AdminDefaulSettings(Exception):
    pass


def add_booking_settings(duration, start_time, admin_id):
    try:
        settings = models.BookingSettings(duration=duration, start_time=start_time, admin_id=admin_id)
        models.db.session.add(settings)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise AdminDefaulSettings('Failed to add default settings')
