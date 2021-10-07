import base64
from tools.add_slot_from_db_for_schedule_admin import add_slot_from_db_for_schedule_admin
from tools.create_db_for_tests import create_test_app_with_db
from db.models import Slots, SlotsShema
import db.models as models
import server as app
from tools.for_db.work_with_admin_info import add_admin
from tools.func_for_psw import password_hashing
json = [
    {
        'end_interval': '2021-03-04T10:00',
        'booking_id': None,
        'start_interval': '2021-03-03T10:00',
        'id': 1
    }
]
admin_email = 'test@test.test'
admin_psw = 'testtest'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


def test_add_slots_in_db():
    create_test_app_with_db()
    add_admin(admin_email, password_hashing(admin_psw))
    add_slot_from_db_for_schedule_admin("2021-03-03T10:00", "2021-03-04T10:00", admin_email)
    req = add_slot_from_db_for_schedule_admin("2021-03-03T10", "2021-03-04T10:00", admin_email)
    id = Slots.query.order_by(Slots.id.desc()).limit(1)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(id)
    assert output == json
    assert req == "400 Bad Request"


def test_status_200():
    with app.app.test_client() as con:
        response = con.post('/schedule/start=2021-03-02T11:00&end=2021-04-03T12:00', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'


def test_resp_json():
    with app.app.test_client() as con:
        response = con.post('/schedule/start=2021-03-02T12:00&end=2021-04-03T12:00', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.json == [{'booking_id': None, 'end_interval': '2021-04-03T12:00', 'id': 3, 'start_interval': '2021-03-02T12:00'}]
    models.Slots.query.delete()
    models.AdminInfo.query.delete()
