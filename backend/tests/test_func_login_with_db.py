import pytest

from tools.for_db.work_with_admin_info import get_psw_from_db, add_admin
from tools.create_db_for_tests import create_test_app_with_db


@pytest.fixture(scope='module')
def app_for_test():
    create_test_app_with_db()
    yield


def test_admin_repo(app_for_test):
    log = 'admin'
    psw = 'Pyth0n'
    app_for_test

    add_admin(log, psw)

    psw_from_db = get_psw_from_db(log)

    assert psw_from_db == psw
