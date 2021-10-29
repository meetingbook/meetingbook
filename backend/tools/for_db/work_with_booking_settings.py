from db.models import BookingSettings, db


class AdminDefaulSettings(Exception):
    pass


def add_booking_settings(duration, start_time, admin_id):
    try:
        settings = BookingSettings(duration=duration, start_time=start_time, admin_id=admin_id)
        db.session.add(settings)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise AdminDefaulSettings('Failed to add default settings')
    finally:
        db.session.close()


def get_booking_settings_by_admin_id(admin_id):
    return BookingSettings.query.filter_by(admin_id=admin_id).first()
