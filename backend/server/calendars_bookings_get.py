from flask import Blueprint
from flask.json import jsonify
from tools.build_response import build_response
from tools.for_db.work_with_slots import get_slots_by_admin_id_and_booking_id, BookingNotFound
from tools.for_db.work_with_booking_info import get_booking_info
from tools.for_db.work_with_links import get_link
from tools.check_link import check_link, LinkHasExpired, LinkNotFound

calendars_bookings_get = Blueprint('calendars_bookings_get', __name__)


@calendars_bookings_get.route('/calendars/<link_id>/bookings/<booking_id>', methods=['GET'])
def get_calendars_bookings(link_id, booking_id):
    try:
        link = get_link(link_id)
        check_link(link)
        slots = get_slots_by_admin_id_and_booking_id(link.admin_id, booking_id)
        booking_info = get_booking_info(booking_id)
    except BookingNotFound as e:
        return build_response(f'{e}', 404)
    except LinkNotFound as e:
        return build_response(f'{e}', 404)
    except LinkHasExpired as e:
        return build_response(f'{e}', 401)
    return jsonify({
        "id": booking_info.id,
        "guest_name": booking_info.name,
        "guest_email": booking_info.email,
        "topic": booking_info.topic,
        "start": slots.start_interval,
        "end": slots.end_interval
    })
