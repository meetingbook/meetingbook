from db.models import BookingSettings
from tools.get_admin_if_by_email import get_admin_id_by_email
import db.models as models
from tools.build_response import build_response


def put_booking_settings(duration, start_time, email_admin):
    admin_id = get_admin_id_by_email(email_admin)
    try:
        BookingSettings.query.filter_by(admin_id=admin_id).update(dict(duration=duration, start_time=start_time))
        models.db.session.commit()
        return build_response("Successful", 200)
    except Exception as e:
        models.db.session.rollback()
        return build_response(e, 500)
