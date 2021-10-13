from flask import Blueprint

from server.auth import auth
from tools.for_db.work_with_admin_info import get_admin_id

admin_calendar_get = Blueprint('admin_calendar_get', __name__)


@admin_calendar_get.route('/calendars/', methods=['GET'])
@auth.login_required
def admin_calendar_get():
    admin_id = get_admin_id(auth.current_user())


