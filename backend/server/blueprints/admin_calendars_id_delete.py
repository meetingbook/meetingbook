from flask import Blueprint, make_response, jsonify

from server.auth import auth
from tools.for_db.work_with_admin_info import get_admin_id
from tools.for_db.work_with_links import delete_link, get_link

admin_calendars_id = Blueprint('admin_calendars_id', __name__)


@admin_calendars_id.route('/calendars/<link_id>', methods=['DELETE'])
@auth.login_required
def calendars_delete_link(link_id):
    admin_id = get_admin_id(auth.current_user())
    if get_link(link_id) is None:
        return make_response(jsonify({'status': 404, 'detail': 'Shareable link not found'}), 404)
    try:
        delete_link(admin_id, link_id)
    except Exception:
        return make_response(jsonify({'status': 500, 'detail': 'Unable to delete link'}), 500)
    return jsonify({'detail': 'deletion successful'})
