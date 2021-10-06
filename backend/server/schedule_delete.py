from flask import Blueprint
from tools.delete_slot_by_id_for_schedule import delete_slot_by_id_for_schedule

schedule_delete = Blueprint('schedule_delete', __name__)


@schedule_delete.route("/schedule/interval_id=<interval_id>", methods=['DELETE'])
def delete_slots(interval_id):
    """ Delete slots by id
    """
    delete_slot = delete_slot_by_id_for_schedule(interval_id)
    return delete_slot
