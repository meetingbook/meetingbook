from flask import Blueprint
from tools.add_slot_from_db_for_schedule_admin import add_slot_from_db_for_schedule_admin
from server.auth import auth
schedule_post = Blueprint('schedule_post', __name__)


@schedule_post.route("/schedule/start=<start>&end=<end>", methods=['POST'])
@auth.login_required
def new_free_slots_for_admin(start, end):
    """ Filter: booked or available.
        Return JSON with <filter> slots.
    """
    email_admin = auth.current_user()
    add_slot = add_slot_from_db_for_schedule_admin(start, end, email_admin)
    return add_slot
