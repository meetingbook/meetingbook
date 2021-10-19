import uuid
from datetime import date
from flask import make_response, jsonify, Blueprint, request
from flask_expects_json import expects_json
from server.auth import auth
from server.validation.schemas import calendar_link_schema
from tools.for_db.work_with_links import add_link, LinkExistsException
from tools.datetime_convertations import DateTime
calendars_post = Blueprint('calendars_post', __name__)


def get_expiry_date(expiry_date: str) -> date:
    """Sets expiry date for link_for_calendar"""
    if expiry_date is None:
        return DateTime().utc_plus_delta(days=30)
    else:
        return DateTime().convert_to_datetime(expiry_date)


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

    return jsonify({"id": link_id, "valid_until": DateTime().convert_to_iso(valid_until)})
