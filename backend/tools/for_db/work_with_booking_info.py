import db.models as models
from flask import make_response


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
    finally:
        models.db.session.close()
