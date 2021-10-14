from flask import jsonify
from db.models import BookingSettings
from tools.for_db.work_with_admin_info import get_admin_id
import db.models as models
from tools.build_response import build_response
from tools.get_booking_settings import get_booking_settings


def put_booking_settings(duration, start_time, email_admin):
    admin_id = get_admin_id(email_admin)
    try:
        BookingSettings.query.filter_by(admin_id=admin_id).update(dict(duration=duration, start_time=start_time))
        models.db.session.commit()
        return jsonify(get_booking_settings(email_admin))
    except Exception as e:
        models.db.session.rollback()
        return build_response(e, 500)
