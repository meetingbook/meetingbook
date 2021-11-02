from datetime import datetime

import db.models as models
from flask import jsonify
from cli.parser import regular_start_end
from tools.build_response import build_response
from tools.for_db.work_with_admin_info import get_admin_id
from tools.for_db.work_with_slots import add_slot_and_get_id, get_slot_by_id


def add_slot_from_db_for_schedule_admin(start, end, email_admin):
    """Add new free slots in db for admin schedule.
    If the slot is added - return json with this slots.
    If the slot is don't added - return error msg
    """
    if (regular_start_end(start) and regular_start_end(end) and start < end
            and datetime.fromisoformat(start) > datetime.utcnow()):
        try:
            id_admin = get_admin_id(email_admin)
            slots = add_slot_and_get_id(start + ':00.000Z', end + ':00.000Z', id_admin)
            return jsonify(get_slot_by_id(slots))
        except Exception:
            models.db.session.rollback()
            return build_response('Creation failed', 500)
    else:
        return build_response("400 Bad Request", 400)
