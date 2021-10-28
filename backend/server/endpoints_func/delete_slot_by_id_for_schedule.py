from db.models import Slots
import db.models as models
from flask import make_response


def delete_slot_by_id_for_schedule(interval_id):
    try:
        models.db.session.delete(Slots.query.get(interval_id))
        models.db.session.commit()
        return make_response({
            "status": 200,
            "detail": "Successfully deleted"
        }, 200)
    except Exception:
        models.db.session.rollback()
        return make_response({
            "status": 500,
            "detail": "Delete error"
        }, 500)
