from flask import Blueprint, jsonify
from tools.add_slot_from_db_for_schedule_admin import add_slot_from_db_for_schedule_admin

schedule_post = Blueprint('schedule_post', __name__)


@schedule_post.route("/schedule/start=<start>&end=<end>", methods=['POST'])
def new_free_slots_for_admin(start, end):
    """ Filter: booked or available.
        Return JSON with <filter> slots.
    """
    add_slot = add_slot_from_db_for_schedule_admin(start, end)
    return jsonify(add_slot)
