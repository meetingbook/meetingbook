from datetime import datetime

from db.models import Slots
from flask import Blueprint, make_response, jsonify
from db import models
from tools.datetime_convertations import DateTime
from tools.get_slots_by_filter import get_slots_by_filter

guest_calendar_get = Blueprint('guest_calendar_get', __name__)


@guest_calendar_get.route('/calendars/<link_id>', methods=['GET'])
def get_calendar(link_id):
    link = models.Links.query.filter_by(link_id=link_id).first()
    if link is None:
        return make_response(jsonify({'status': 404, 'detail': 'Shareable link not found'}), 404)
    elif DateTime().convert_to_datetime(link.valid_until) < datetime.utcnow():
        return make_response(jsonify({'status': 401, 'detail': 'Unauthorized - link has expired'}), 401)
    return jsonify({
      "id": link.id,
      "valid_until": link.valid_until,
      "slots": get_slots_by_filter('available', link.admin_id, Slots.end_interval > datetime.utcnow())
    })
