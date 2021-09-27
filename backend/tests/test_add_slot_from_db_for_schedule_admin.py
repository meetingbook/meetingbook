from tools.add_slot_from_db_for_schedule_admin import add_slot_from_db_for_schedule_admin
from tools.create_db_for_tests import create_test_app_with_db
from db.models import Slots, SlotsShema
import db.models as models
json = [
    {
        'end_interval': '2021-03-04T10:00',
        'booking_id': None,
        'start_interval': '2021-03-03T10:00',
        'id': 1
    }
]


def test_add_slots_in_db():
    create_test_app_with_db()
    add_slot_from_db_for_schedule_admin("2021-03-03T10:00", "2021-03-04T10:00")
    id = Slots.query.order_by(Slots.id.desc()).limit(1)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(id)
    assert output == json
    models.Slots.query.delete()
