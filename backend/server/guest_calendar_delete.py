from datetime import datetime

from flask import Blueprint
from db.models import db
from tools.build_response import build_response
from tools.datetime_convertations import DateTime
from tools.for_db.work_with_booking_info import delete_booking_info, BookingSlotException
from tools.for_db.work_with_links import get_link
from tools.for_db.work_with_slots import canceling_booking_id_from_slot, DbSlotException

guest_calendar_delete = Blueprint('guest_calendar_delete', __name__)


@guest_calendar_delete.route('/calendars/<link_id>/bookings/<booking_id>', methods=['DELETE'])
def canceling_booking(link_id, booking_id):
    link = get_link(link_id)
    if link is None:
        return build_response('Shareable link not found', 404)
    elif DateTime().convert_to_datetime(link.valid_until) < datetime.utcnow():
        return build_response('Unauthorized - link has expired', 401)
    try:
        canceling_booking_id_from_slot(booking_id)
        delete_booking_info(booking_id)
        db.session.commit()
        return build_response('Successful request', 200)
    except (DbSlotException, BookingSlotException) as e:
        build_response(e, 409)
        db.session.rollback()
    finally:
        db.session.close()
