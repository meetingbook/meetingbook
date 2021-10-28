import base64
from datetime import datetime, timedelta

from server.endpoints_func.add_slot_from_db_for_schedule_admin import add_slot_from_db_for_schedule_admin
from db.models import Slots, SlotsShema
from tools.for_db.work_with_admin_info import add_admin
from tools.func_for_psw import password_hashing


def dt(delta):
    return (datetime.utcnow() + timedelta(hours=delta)).isoformat(timespec='minutes')


start = dt(1)
end = dt(2)
json = [
    {
        'end_interval': end + ':00.000Z',
        'booking_id': None,
        'start_interval': start + ':00.000Z',
        'id': 1
    }
]
admin_email = 'test@test.test'
admin_psw = 'testtest'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


def test_add_slots_in_db(app_for_test):
    add_admin(admin_email, password_hashing(admin_psw))
    add_slot_from_db_for_schedule_admin(start, end, admin_email)
    req = add_slot_from_db_for_schedule_admin("2021-03-03T10", "2021-03-04T10:00", admin_email)
    id = Slots.query.order_by(Slots.id.desc()).limit(1)
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(id)
    assert output == json
    assert req.status == '400 BAD REQUEST'


def test_status_200(app_for_test):
    start = dt(3)
    end = dt(4)
    response = app_for_test.post(f'/schedule/start={start}&end={end}', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'


def test_resp_json(app_for_test):
    start = dt(4)
    end = dt(5)
    response = app_for_test.post(f'/schedule/start={start}&end={end}', headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.json == {'id': 3, 'booking_id': None,
                             'end_interval': end + ':00.000Z', 'start_interval': start + ':00.000Z'}
