from flask import Blueprint, jsonify

from server.auth import auth
from tools.for_db.work_with_admin_info import get_admin_id
from tools.for_db.work_with_links import query_links

admin_calendar_get = Blueprint('admin_calendar_get', __name__)


@admin_calendar_get.route('/calendars/', methods=['GET'])
@auth.login_required
def get_calendar():
    admin_id = get_admin_id(auth.current_user())
    return jsonify({'links': query_links(admin_id)})
