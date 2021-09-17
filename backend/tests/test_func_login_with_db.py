import pytest

from tools.create_db_for_tests import create_test_app_with_db
from tools.work_with_db import get_psw_from_db
import db.models as models


@pytest.fixture(scope='module')
def app_for_test():
    create_test_app_with_db()
    yield
    models.AdminInfo.query.delete()


def test_get_psw_from_db(app_for_test):
    log = 'admin'
    psw = 'Pyth0n'
    app_for_test
    test_admin = models.AdminInfo(email=log, psw=psw)
    models.db.session.add(test_admin)
    models.db.session.commit()
    psw_from_db = get_psw_from_db(log)

    assert psw_from_db == psw
