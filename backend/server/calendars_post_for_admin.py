import uuid
from flask import make_response, jsonify, Blueprint, request
from server.auth import auth
from flask_httpauth import HTTPBasicAuth
from flask_expects_json import expects_json
from server.validation.schemas import calendar_link_schema
calendars_post = Blueprint('register_blueprint', __name__)
from db.models import AdminInfo
register_blueprint = Blueprint('register_blueprint', __name__)
from db.models import AdminInfo, LinksSchema
from tools.for_db.work_with_links import add_link

register_blueprint = Blueprint('register_blueprint', __name__)
from tools.for_db.work_with_admin_info import get_admin_id


@calendars_post.route('/calendars', methods=['POST'])
@auth.login_required
@expects_json(LinksSchema)

def set_default_expiry_date():
    '''Sets default expiry date for link_for_calendar in case Admin doesn't send "valid_until" parameter'''
    default_expiry_date = DateTime.today() + RelativeDelta(days=30)
    return default_expiry_date


def set_expiry_date():
'''Sets expiry date for link_for_calendar'''
    if expiry_date is None:
        return set_default_expiry_date()
    else:
        return expiry_date

def generate_link_id() -> string:
'''Generates link_id for calendar created by Admin'''
    link_id = uuid.uuid4()
    return link_id

def get_admin_id_from_auth() -> string:
    admin_id = auth.current_user().id
    return admin_id

if request.method == 'POST':
        expiry_date = request.get_json(force=True)('valid_until')
        set_expiry_date()
        generate_link_id()





def add_info_to_links_table():
    try:
        admin_id = get_admin_id()
        link_id = generate_link_id()
        valid_until = set_expiry_date()
        add_link(link_id, valid_until, admin_id)
    except AdminExistsException:
        return make_response(jsonify({"status": 409,
                                      'detail': 'Conflict. This email is already registered in MeetingBook'}), 409)
    return jsonify({'detail': 'Successful registration'})


@error_handler(ValueError)
def value_error():
    return make_response({
        "status": 400,
        "detail": "Invalid format string"
    }, 400)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'status': 401, 'detail': 'Unauthorized'}), 401)


