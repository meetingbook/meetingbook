from datetime import datetime

from flask import Blueprint
from db.models import db
from tools.build_response import build_response
from tools.datetime_convertations import DateTime
from tools.for_db.work_with_booking_info import delete_booking_info_and_get_id, BookingSlotException
from tools.for_db.work_with_links import get_link
from tools.for_db.work_with_slots import canceling_booking_id_from_slot, DbSlotException

guest_calendar_delete = Blueprint('guest_calendar_delete', __name__)


@guest_calendar_delete.route('/calendars/<link_id>/bookings/<booking_uuid>', methods=['DELETE'])
def canceling_booking(link_id, booking_uuid):
    link = get_link(link_id)
    if link is None:
        return build_response('Shareable link not found', 404)
    elif DateTime().convert_to_datetime(link.valid_until) < datetime.utcnow():
        return build_response('Unauthorized - link has expired', 401)
    try:
        booking_id = delete_booking_info_and_get_id(booking_uuid)
        canceling_booking_id_from_slot(booking_id, link.admin_id)
        db.session.commit()
        return build_response('Successful request', 200)
    except (DbSlotException, BookingSlotException) as e:
        db.session.rollback()
        return build_response(f'{e}', 409)
    finally:
        db.session.close()
