from flask import Blueprint, request, make_response
from flask_expects_json import expects_json
from server.validation.schemas import guest_calendar_schema
from tools.emails import send_email
from tools.for_db.work_with_booking_info import add_booking_info_and_get_uuid
from tools.for_db.work_with_links import get_link
from tools.build_response import build_response

guest_calendar_post = Blueprint('guest_calendar_post', __name__)


def create_guest_calendar_post(mail):
    guest_calendar_post = Blueprint('guest_calendar_post', __name__)

    @guest_calendar_post.route('/calendars/<link_id>/bookings/', methods=['POST'])
    @expects_json(guest_calendar_schema)
    def booking(link_id):
        request_body = request.get_json()
        link = get_link(link_id)
        if link is None:
            return build_response('link id is invalid', 401)
        admin_id = link.admin_id
        try:
            uuid = add_booking_info_and_get_uuid(request_body['start'], request_body['end'], admin_id,
                                                 request_body['guest_name'], request_body['guest_email'],
                                                 request_body['topic'] if 'topic' in request_body else None)
            request_body['uuid'] = uuid
        except Exception:
            return make_response({"status": 409, "detail": 'already booked or deleted'}, 409)
        send_email(admin_id, request_body, mail, link_id)
        return make_response(request_body, 200)
    return guest_calendar_post
