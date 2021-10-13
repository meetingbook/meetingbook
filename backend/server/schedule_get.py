from flask import Blueprint, jsonify, make_response
from tools.for_db.work_with_admin_info import get_admin_id
from tools.get_slots_by_filter import get_slots_by_filter
from tools.get_slots_from_db_for_schedule import get_slots_from_db_for_schedule
from server.auth import auth

schedule_get = Blueprint('schedule_get', __name__)


@schedule_get.route("/schedule/status=<filter>", methods=['GET'])
@auth.login_required
def slot_by_filter(filter):
    admin_id = get_admin_id(auth.current_user())
    """ Filter: booked or available.
        Return JSON with <filter> slots.
    """
    return jsonify({'slots': get_slots_by_filter(filter, admin_id)})


@schedule_get.route("/schedule/day=<date>/", defaults={'filter': None}, methods=['GET'])
@schedule_get.route("/schedule/day=<date>&status=<filter>", methods=['GET'])
@auth.login_required
def slot_in_day_by_filter(date, filter):
    admin_id = get_admin_id(auth.current_user())
    """ Filter: booked or available.
        Return JSON of <filter> slots for the <date>
    """
    return jsonify({'slots': get_slots_from_db_for_schedule(admin_id, date, filter, 1)})


@schedule_get.route("/schedule/week=<date>/", defaults={'filter': None}, methods=['GET'])
@schedule_get.route("/schedule/week=<date>&status=<filter>", methods=['GET'])
@auth.login_required
def slot_in_week_by_filter(date, filter):
    admin_id = get_admin_id(auth.current_user())
    """ Filter: booked or available.
        Return JSON of <filter> slots for the week starting from <date>.
    """
    return jsonify({'slots': get_slots_from_db_for_schedule(admin_id, date, filter, 7)})


@schedule_get.errorhandler(ValueError)
def value_error(e):
    return make_response({
        "status": 400,
        "detail": "Invalid isoformat string"
    }, 400)


@schedule_get.errorhandler(Exception)
def exception(e):
    return make_response({
        "status": 500,
        "detail": "Other exception"
    }, 500)
