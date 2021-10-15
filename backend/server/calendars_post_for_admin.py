import uuid
from datetime import date, timedelta
from flask import make_response, jsonify, Blueprint, request
from flask_expects_json import expects_json
from server.auth import auth
from server.converters.datetime_converters import str_to_iso8601, iso8601_to_str
from server.validation.schemas import calendar_link_schema
from tools.for_db.work_with_links import add_link, LinkExistsException

calendars_post = Blueprint('calendars_post', __name__)


def get_default_expiry_date() -> date:
    """Returns default expiry date for link_for_calendar in case Admin doesn't send "valid_until" parameter"""
    return date.today() + timedelta(days=30)


def get_expiry_date(expiry_date: str) -> date:
    """Sets expiry date for link_for_calendar"""
    if expiry_date is None:
        return get_default_expiry_date()
    else:
        return str_to_iso8601(expiry_date)


def generate_link_id() -> str:
    """Generates link_id for calendar created by Admin"""
    return str(uuid.uuid4())


@calendars_post.route('/calendars', methods=['POST'])
@expects_json(calendar_link_schema, check_formats=True)
@auth.login_required
def add_info_to_links_table():
    expiry_date = request.json['valid_until'] if request.json else None
    admin_email = auth.current_user()
    link_id = generate_link_id()
    valid_until = get_expiry_date(expiry_date)

    try:
        add_link(link_id, valid_until, admin_email)
    except LinkExistsException:
        return make_response(jsonify({
            "status": 409,
            "detail": "Conflict. This link exists in MeetingBook"
        }), 409)

    return jsonify({"id": link_id, "valid_until": iso8601_to_str(valid_until)})
