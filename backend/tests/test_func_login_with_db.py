import pytest

from domain.entities.admin import Admin
from tools.for_db.work_with_admin_info import get_psw_from_db, add_admin
from tools.create_db_for_tests import create_test_app_with_db
import db.models as models


@pytest.fixture(scope='module')
def app_for_test():
    create_test_app_with_db()
    yield
    models.AdminInfo.query.delete()


def test_admin_repo(app_for_test):
    log = 'admin'
    psw = 'Pyth0n'
    test_admin = Admin(log, psw)
    app_for_test

    add_admin(test_admin)

    psw_from_db = get_psw_from_db(test_admin.get_email())

    assert psw_from_db == psw
