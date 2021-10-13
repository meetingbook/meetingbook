from datetime import datetime

from flask import Blueprint, make_response, jsonify
from db import models
from tools.get_slots_by_filter import get_slots_by_filter

guest_calendar_get = Blueprint('guest_calendar_get', __name__)


@guest_calendar_get.route('/calendar/<link_id>', methods=['GET'])
def guest_calendar_get(link_id):
    link = models.Links.query.filter_by(link_id=link_id).first()
    if link is None:
        return make_response(jsonify({'status': 404, 'detail': 'Shareable link not found'}), 404)
    elif datetime.fromisoformat(link.valid_until) < datetime.utcnow():
        return make_response(jsonify({'status': 401, 'detail': 'Unauthorized - link has expired'}), 401)
    return jsonify({
      "id": link.id,
      "valid_until": link.valid_until,
      "slots": get_slots_by_filter(link.admin_id, 'available')
    })
