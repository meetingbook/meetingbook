from db.models import Slots
import db.models as models


def delete_slot_by_id_for_schedule(interval_id):
    try:
        models.db.session.delete(Slots.query.get(interval_id))
        models.db.session.commit()
        return {
            'msg': 'successfully deleted'
        }
    except Exception:
        models.db.session.rollback()
        return {
            'msg': 'delete error'
        }
