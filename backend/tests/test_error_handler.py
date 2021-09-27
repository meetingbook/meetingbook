import server as app
import pytest
from tools.create_db_for_tests import create_test_app_with_db


@pytest.mark.parametrize("date", [("/schedule/week=2021-15-25&filter=booking"),
                                  ("/schedule/week=2021-05-40&filter=booking"),
                                  ("/schedule/day=2021-15-25&filter=booking"),
                                  ("/schedule/day=2021-05-40&filter=available")])
def test_status_400(date):
    app.app.config['TESTING'] = True
    test_app = app.app.test_client()
    response = test_app.get(date)
    assert response.status == '400 BAD REQUEST'


@pytest.mark.parametrize("date", [("/schedule/week=2021-10-25&filter=booking"),
                                  ("/schedule/week=2021-05-10&filter=available"),
                                  ("/schedule/day=2021-10-25&filter=booking"),
                                  ("/schedule/day=2021-10-25&filter=available")])
def test_status_200(date):
    create_test_app_with_db()
    app.app.config['TESTING'] = True
    test_app = app.app.test_client()
    response = test_app.get(date)
    assert response.status == '200 OK'


@pytest.mark.parametrize("date", [("/schedule/test=2021-10-25&filter=booking")])
def test_status_404(date):
    app.app.config['TESTING'] = True
    test_app = app.app.test_client()
    response = test_app.get(date)
    assert response.status == '404 NOT FOUND'
