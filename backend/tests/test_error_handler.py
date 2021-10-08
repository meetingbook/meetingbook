import server as app
import pytest
from tools.create_db_for_tests import create_test_app_with_db


@pytest.mark.parametrize("date", [("/schedule/week=2021-15-25&status=booking"),
                                  ("/schedule/week=2021-05-40&status=booking"),
                                  ("/schedule/day=2021-15-25&status=booking"),
                                  ("/schedule/day=2021-05-40&status=available")])
def test_status_400(date):
    with app.app.test_client() as con:
        response = con.get(date)
    assert response.status == '400 BAD REQUEST'


@pytest.mark.parametrize("date", [("/schedule/week=2021-10-25&status=booking"),
                                  ("/schedule/week=2021-05-10&status=available"),
                                  ("/schedule/day=2021-10-25&status=booking"),
                                  ("/schedule/day=2021-10-25&status=available")])
def test_status_200(date):
    create_test_app_with_db()
    with app.app.test_client() as con:
        response = con.get(date)
    assert response.status == '200 OK'


@pytest.mark.parametrize("date", [("/schedule/test=2021-10-25&status=booking")])
def test_status_404(date):
    with app.app.test_client() as con:
        response = con.get(date)
    assert response.status == '404 NOT FOUND'
