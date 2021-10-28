from tools.for_test.create_db_for_tests import create_test_app_with_db
from server.endpoints_func.delete_slot_by_id_for_schedule import delete_slot_by_id_for_schedule
import db.models as models


def test_delete_schedule_slot_if_not_id():
    create_test_app_with_db()
    resp = delete_slot_by_id_for_schedule(1)
    assert resp.json == {
        "detail": "Delete error",
        "status": 500
    }


def test_delete_slot_schedule():
    start_interval = "2021-02-03T10:00"
    end_interval = "2021-02-03T12:00"
    json = {
        "status": 200,
        "detail": "Successfully deleted"
    }
    slots = models.Slots(start_interval=start_interval, end_interval=end_interval)
    models.db.session.add(slots)
    models.db.session.commit()
    resp = delete_slot_by_id_for_schedule(1)
    assert resp.json == json
