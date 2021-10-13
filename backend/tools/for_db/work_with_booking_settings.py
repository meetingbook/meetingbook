import db.models as models
from flask import make_response


class AdminDefaulSettings(Exception):
    pass


def add_booking_settings(duration, start_time, admin_id):
    try:
        settings = models.BookingSettings(duration=duration, start_time=start_time, admin_id=admin_id)
        models.db.session.add(settings)
        models.db.session.commit()
    except Exception as e:
        return make_response({
            "status": 500,
            "detail": f"{e}"
        }, 500)
    finally:
        models.db.session.close()
