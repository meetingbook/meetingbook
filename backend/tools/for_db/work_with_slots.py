import db.models as models
from flask import make_response


def add_slots(start_interval, end_interval, create_admin_id, booking_id=None):
    try:
        slots = models.Slots(start_interval=start_interval, end_interval=end_interval,
                             booking_id=booking_id, admin_id=create_admin_id)
        models.db.session.add(slots)
        models.db.session.commit()
    except Exception as e:
        return make_response({
            "status": 500,
            "detail": f"{e}"
        }, 500)
    finally:
        models.db.session.close()
