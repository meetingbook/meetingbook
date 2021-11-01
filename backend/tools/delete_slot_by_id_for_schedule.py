from db.models import Slots
import db.models as models
from tools.build_response import build_response


def delete_slot_by_id_for_schedule(interval_id):
    try:
        models.db.session.delete(Slots.query.get(interval_id))
        models.db.session.commit()
        return build_response("Successfully deleted", 200)
    except Exception:
        models.db.session.rollback()
        return build_response("Delete error", 500)
