from flask import Blueprint, request, make_response, jsonify
import db.models as models
from tools.for_db.work_with_booking_info import booking_slot, BookingSlotException

guest_calendar_post = Blueprint('guest_calendar_post', __name__)


def get_admin_id_by_link_id(link_id):
    try:
        link = models.Links.query.filter_by(link_id=link_id).first()
        return link.admin_id
    except Exception:
        return make_response(jsonify({'status': 401, 'detail': 'link id is invalid'}), 401)


@guest_calendar_post.route('/calendar/<str:link_id>/bookings/', methods=['POST'])
def booking(linked_id):
    try:
        request_body = request.get_json()
        admin_id = get_admin_id_by_link_id(linked_id)
        booking_slot(request_body['guest_name'], request_body['guest_email'], request_body['topic'] or None,
                     request_body['start'], request_body['end'], admin_id)
    except BookingSlotException:
        make_response({"status": 409, "detail": "already booked or deleted"}, 409)
