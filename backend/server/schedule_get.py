from flask import Blueprint, jsonify
from tools.get_slot_by_filter import get_slot_by_filter
from tools.get_slot_in_week import get_slot_in_week
from tools.get_slot_in_day import get_slot_in_day
from tools.get_slots_in_week_by_filter import get_slots_in_week_by_filter
from tools.get_slots_in_day_by_filter import get_slots_in_day_by_filter


schedule_get = Blueprint('schedule_get', __name__)


@schedule_get.route("/schedule/filter=status=<filter>", methods=['GET'])
def slot_by_filter(filter):
    """ Filter: booked or available.
        Return JSON with <filter> slots.
    """
    return jsonify(get_slot_by_filter(filter))


@schedule_get.route("/schedule/week=<date>", methods=['GET'])
def slot_in_week(date):
    """ Return JSON slots for the week starting from <date>
    """
    return jsonify(get_slot_in_week(date))


@schedule_get.route("/schedule/day=<date>", methods=['GET'])
def slot_in_day(date):
    """ Return JSON of slots for the day <date>
    """
    return jsonify(get_slot_in_day(date))


@schedule_get.route("/schedule/week=<date>&filter=<filter>", methods=['GET'])
def slot_in_week_by_filter(date, filter):
    """ Filter: booked or available.
        Return JSON of <filter> slots for the week starting from <date>.
    """
    return jsonify(get_slots_in_week_by_filter(date, filter))


@schedule_get.route("/schedule/day=<date>&filter=<filter>", methods=['GET'])
def slot_in_day_by_filter(date, filter):
    """ Filter: booked or available.
        Return JSON of <filter> slots for the <date>
    """
    return jsonify(get_slots_in_day_by_filter(date, filter))
