from datetime import datetime

import db.models as models
from db.models import Slots, SlotsShema, AdminInfo
from flask import make_response, jsonify
from cli.parser import regular_start_end


def add_slot_from_db_for_schedule_admin(start, end, email_admin):
    """Add new free slots in db for admin schedule.
    If the slot is added - return json with this slots.
    If the slot is don't added - return error msg
    """
    if (regular_start_end(start) and regular_start_end(end) and start < end
            and datetime.fromisoformat(start) > datetime.utcnow()):
        try:
            query_get_id_admin = AdminInfo.query.with_entities(AdminInfo.id).filter(AdminInfo.email == email_admin)
            id_admin = query_get_id_admin[0]["id"]
            slots = models.Slots(start_interval=start, end_interval=end, admin_id=id_admin)
            models.db.session.add(slots)
            models.db.session.commit()
            return jsonify(get_last_slot_id(slots.id))
        except Exception:
            models.db.session.rollback()
            return make_response({'detail': 'Creation failed', 'status': 500}, 500)
    else:
        return make_response({'detail': "400 Bad Request", 'status': 400}, 400)


def get_last_slot_id(slots_id):
    id_added_slots = Slots.query.filter(Slots.id == slots_id)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(id_added_slots)
    return output
