import pytest
from tools.create_db_for_tests import create_test_app_with_db
from tools.for_db.work_with_admin_info import add_admin
from tools.func_for_psw import password_hashing
import base64

admin_email = 'test@test.test'
admin_psw = 'testtest'
valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


@pytest.mark.parametrize("date", [("/schedule/test=2021-10-25&status=booking")])
def test_status_404(date):
    with create_test_app_with_db().test_client() as con:
        add_admin(admin_email, password_hashing(admin_psw))
        response = con.get(date, headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '404 NOT FOUND'


@pytest.mark.parametrize("date", [("/schedule/week=2021-15-25&status=booking"),
                                  ("/schedule/week=2021-05-40&status=booking"),
                                  ("/schedule/day=2021-15-25&status=booking"),
                                  ("/schedule/day=2021-05-40&status=available")])
def test_status_400(date):
    with create_test_app_with_db().test_client() as con:
        add_admin(admin_email, password_hashing(admin_psw))
        response = con.get(date, headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '400 BAD REQUEST'


@pytest.mark.parametrize("date", [("/schedule/week=2021-10-25&status=booking"),
                                  ("/schedule/week=2021-05-10&status=available"),
                                  ("/schedule/day=2021-10-25&status=booking"),
                                  ("/schedule/day=2021-10-25&status=available")])
def test_status_200(date):
    with create_test_app_with_db().test_client() as con:
        add_admin(admin_email, password_hashing(admin_psw))
        response = con.get(date, headers={'Authorization': 'Basic ' + valid_credentials})
    assert response.status == '200 OK'
