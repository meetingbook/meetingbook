from flask import Blueprint, make_response, jsonify
from db import models
from tools.get_slots_by_filter import get_slots_by_filter

guest_calendar_get = Blueprint('guest_calendar_get', __name__)


@guest_calendar_get.route('/calendar/<link_id>', methods=['GET'])
def guest_calendar_get(link_id):
    link = models.Links.query.filter_by(link_id=link_id).first()
    if link is None:
        return make_response(jsonify({'status': 401, 'detail': 'link id is invalid'}), 401)
    get_slots_by_filter('available', link.admin_id)
