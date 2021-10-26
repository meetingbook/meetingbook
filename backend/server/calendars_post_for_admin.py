import uuid
from datetime import date
from flask import make_response, jsonify, Blueprint, request
from flask_expects_json import expects_json
from server.auth import auth
from server.validation.schemas import calendar_link_schema
from tools.for_db.work_with_links import add_link, LinkExistsException
from tools.datetime_convertations import DateTime
from tools.for_db.work_with_admin_info import get_admin_id

calendars_post = Blueprint('calendars_post', __name__)


def get_expiry_date(data: object = {}) -> date:
    """Sets expiry date for link_for_calendar"""
    if 'data' in data and 'valid_until' in data['data']:
        return data['data']['valid_until']

    return DateTime().utc_plus_delta(days=30)


def generate_link_id() -> str:
    """Generates link_id for calendar created by Admin"""
    return str(uuid.uuid4())


@calendars_post.route('/calendars', methods=['POST'])
@expects_json(calendar_link_schema, check_formats=True)
@auth.login_required
def add_info_to_links_table():
    data = request.get_json('data')
    admin_id = get_admin_id(auth.current_user())
    link_id = generate_link_id()
    valid_until = get_expiry_date(data)

    try:
        add_link(link_id, admin_id, valid_until)
    except LinkExistsException:
        return build_response('Conflict. This link exists in MeetingBook', 409)

    return jsonify({"id": link_id, "valid_until": valid_until})
