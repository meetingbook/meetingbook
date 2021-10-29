from flask import Blueprint, request, make_response, jsonify
from flask_expects_json import expects_json

from server.validation.schemas import guest_calendar_schema
from tools.build_response import build_response
from tools.datetime_convertations import DateTime
from tools.for_db.work_with_booking_info import add_booking_info_and_get_id, get_uuid
from tools.for_db.work_with_booking_settings import get_booking_settings_by_admin_id
from tools.for_db.work_with_links import get_link

guest_calendar_post = Blueprint('guest_calendar_post', __name__)


def check_booking_settings(start, end, booking_settings):
    dt_start = DateTime().convert_to_datetime(start)
    dt_end = DateTime().convert_to_datetime(end)
    delta = dt_end - dt_start
    delta_minutes = str(delta.seconds // 60)
    if (start[14:16] not in booking_settings.start_time['allowed_values']
            or delta_minutes not in booking_settings.duration['allowed_values']):
        return False
    return True


@guest_calendar_post.route('/calendars/<link_id>/bookings/', methods=['POST'])
@expects_json(guest_calendar_schema)
def booking(link_id):
    request_body = request.get_json()
    link = get_link(link_id)
    if link is None:
        return make_response(jsonify({'status': 401, 'detail': 'link id is invalid'}), 401)
    admin_id = link.admin_id
    booking_settings = get_booking_settings_by_admin_id(admin_id)
    if not check_booking_settings(request_body['start'], request_body['end'], booking_settings):
        return build_response('the interval must match booking_settings', 409)
    try:
        booking_id = add_booking_info_and_get_id(request_body['start'], request_body['end'], admin_id,
                                                 request_body['guest_name'], request_body['guest_email'],
                                                 request_body['topic'] if 'topic' in request_body else None)
        request_body['uuid'] = get_uuid(booking_id)
    except Exception:
        return make_response({"status": 409, "detail": 'already booked or deleted'}, 409)
    return make_response(request_body, 200)
