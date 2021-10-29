from flask import Blueprint
from tools.build_response import build_response
from server.auth import auth
from tools.for_db.work_with_admin_info import get_admin_id
from tools.for_db.work_with_links import delete_link, get_link

admin_calendars_id = Blueprint('admin_calendars_id', __name__)


@admin_calendars_id.route('/calendars/<link_id>', methods=['DELETE'])
@auth.login_required
def calendars_delete_link(link_id):
    admin_id = get_admin_id(auth.current_user())
    if get_link(link_id) is None:
        return build_response('Shareable link not found', 404)
    try:
        delete_link(admin_id, link_id)
    except Exception:
        return build_response('Unable to delete link', 500)
    return build_response('Deletion successful', 200)
