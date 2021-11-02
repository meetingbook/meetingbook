from datetime import datetime
from tools.for_db.work_with_links import get_link
from db.models import Slots
from flask import Blueprint, jsonify
from tools.get_slots_by_filter import get_slots_by_filter
from tools.build_response import build_response
from server.validation.ensure_valid_link import ensure_valid_link, LinkNotFound, LinkHasExpired

guest_calendar_get = Blueprint('guest_calendar_get', __name__)


@guest_calendar_get.route('/calendars/<link_id>', methods=['GET'])
def get_calendar(link_id):
    try:
        link = get_link(link_id)
        ensure_valid_link(link)
    except LinkNotFound as e:
        return build_response(f'{e}', 404)
    except LinkHasExpired as e:
        return build_response(f'{e}', 401)
    return jsonify({
        "id": link.id,
        "valid_until": link.valid_until,
        "slots": get_slots_by_filter('available', link.admin_id, Slots.end_interval > datetime.utcnow())
    })
