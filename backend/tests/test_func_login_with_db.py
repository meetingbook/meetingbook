import pytest

from domain.entities.admin import Admin
from domain.repositories.admin_repository import AdminDbRepository
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

    AdminDbRepository().add_admin(test_admin)

    psw_from_db = AdminDbRepository().get_psw_from_db(test_admin.get_email())

    assert psw_from_db == psw
