from flask import Blueprint, request, make_response, jsonify
import db.models as models
from tools.for_db.work_with_booking_info import add_booking_info_and_get_id
from tools.for_db.work_with_slots import get_id_slice_of_slot, update_booking_id_in_slot

guest_calendar_post = Blueprint('guest_calendar_post', __name__)


@guest_calendar_post.route('/calendar/<link_id>/bookings/', methods=['POST'])
def booking(link_id):
    request_body = request.get_json()
    link = models.Links.query.filter_by(link_id=link_id).first()
    if link is None:
        return make_response(jsonify({'status': 401, 'detail': 'link id is invalid'}), 401)
    admin_id = link.admin_id
    try:
        booking_id = add_booking_info_and_get_id(request_body['guest_name'],
                                                 request_body['guest_email'],
                                                 request_body['topic'] or None)
        slot_id = get_id_slice_of_slot(request_body['start'], request_body['end'], admin_id)
        update_booking_id_in_slot(slot_id, booking_id)
    except Exception:
        return make_response({"status": 409, "detail": 'already booked or deleted'}, 409)
    return make_response({"detail": "Successful booked"}, 200)
