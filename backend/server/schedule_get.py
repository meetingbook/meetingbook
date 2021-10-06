from flask import Blueprint, jsonify, make_response
from tools.get_slots_by_filter import get_slots_by_filter
from tools.get_slots_from_db_for_schedule import get_slots_from_db_for_schedule

schedule_get = Blueprint('schedule_get', __name__)


@schedule_get.route("/schedule/status=<filter>", methods=['GET'])
def slot_by_filter(filter):
    """ Filter: booked or available.
        Return JSON with <filter> slots.
    """
    return jsonify({'slots': get_slots_by_filter(filter)})


@schedule_get.route("/schedule/day=<date>/", defaults={'filter': None}, methods=['GET'])
@schedule_get.route("/schedule/day=<date>&status=<filter>", methods=['GET'])
def slot_in_day_by_filter(date, filter):
    """ Filter: booked or available.
        Return JSON of <filter> slots for the <date>
    """
    return jsonify({'slots': get_slots_from_db_for_schedule(date, filter, 1)})


@schedule_get.route("/schedule/week=<date>/", defaults={'filter': None}, methods=['GET'])
@schedule_get.route("/schedule/week=<date>&status=<filter>", methods=['GET'])
def slot_in_week_by_filter(date, filter):
    """ Filter: booked or available.
        Return JSON of <filter> slots for the week starting from <date>.
    """
    return jsonify({'slots': get_slots_from_db_for_schedule(date, filter, 7)})


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
