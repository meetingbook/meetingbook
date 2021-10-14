import uuid
from datetime import datetime as DateTime
from dateutil.relativedelta import relativedelta as RelativeDelta
from flask import make_response, jsonify, Blueprint, request
from server.auth import auth
from flask_httpauth import HTTPBasicAuth
from flask_expects_json import expects_json
from server.validation.schemas import calendar_link_schema
calendars_post = Blueprint('register_blueprint', __name__)
from db.models import AdminInfo
register_blueprint = Blueprint('register_blueprint', __name__)



@calendars_post.route('/calendars', methods=['POST'])
@auth.login_required
@expects_json(calendar_link_schema)

if request.method == 'POST':
        expiry_date = request.get_json(force=True)('valid_until')
else:

    
def generate_calendar_link_id():
'''Generates link_id for calendar created by Admin'''
    link_for_calendars = uuid.uuid4()
    return jsonify({"calendars_id": link_for_calendars})

def set_default_expiry_date():
'''Sets default expiry date for link_for_calendar in case Admin doesn't send "valid_until" parameter'''
    default_expiry_date = DateTime.today() + RelativeDelta(days=30)
    return default_expiry_date

def set_expiry_date():
'''Sets expiry date for link_for_calenda'''
    if expiry_date is None:
        return jsonify ({'valid_until': set_default_expiry_date()})
    else:
        return jsonify ({'valid_until': str(expiry_date})

def get_id_admin():
'''Gets AdminId from authentication'''
        query_get_id_admin = AdminInfo.query.with_entities(AdminInfo.id).filter(AdminInfo.email == email_admin)
        id_admin = query_get_id_admin[0]["id"]
   return id_admin

def add_info_to_calendars_table():
    return jsonify (
        {
        'admin_id': get_id_admin(),
        'calendar_link': generate_calendar_link_id(),
        'valid_until': set_expiry_date()
    }
    )

@error_handler(ValueError)
def value_error():
    return make_response({
        "status": 400,
        "detail": "Invalid format string"
    }, 400)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'status': 401, 'detail': 'Unauthorized'}), 401)


#curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "fizz bizz"}' http://localhost:5000/foo