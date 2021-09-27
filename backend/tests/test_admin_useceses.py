import pytest

import db.models as models
from domain.use_cases.admin_usecases import AdminRegister
from domain.repositories.admin_repository import AdminDbRepository
from tools.create_db_for_tests import create_test_app_with_db
from tools.func_for_psw import check_psw


@pytest.fixture(scope='module')
def app_for_test():
    app_for_test = create_test_app_with_db()
    test_app = app_for_test.test_client()
    yield test_app
    models.AdminInfo.query.delete()


def test_admin_register(app_for_test):
    email = 'mail@.com'
    password = 'Password'
    AdminRegister(email, password).admin_register()
    psw_from_db = AdminDbRepository(models).get_psw_from_db(email)

    assert check_psw(password, psw_from_db)
