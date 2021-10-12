import db.models as models


def add_booking_settings(duration, start_time, admin_id):
    settings = models.BookingSettings(duration=duration, start_time=start_time, admin_id=admin_id)
    models.db.session.add(settings)
    models.db.session.commit()
